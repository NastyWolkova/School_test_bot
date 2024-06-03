from aiogram import Router, F
from fsmstatus import FSMStatus
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile, BufferedInputFile
from aiogram.filters import or_f
from lexicon.lexicon import tasks_log, answers, users 
import datetime
from keyboards import keyboard_cancel, keyboard_rus, keyboard_log_tasks
from functions import conv_time


router: Router = Router()

#ТЕСТИРОВАНИЕ, получение первого задания (и смена статуса юзера)
@router.callback_query(F.data == 'start_pressed', FSMStatus.status_log)
async def process_button_4_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    dt1 = datetime.datetime.today()
    dt2 = dt1 + datetime.timedelta(minutes=60)
    users[callback.from_user.id]['current_task'] = 1
    users[callback.from_user.id]['start'] = dt1
    users[callback.from_user.id]['finish'] = dt2
    await state.set_state(FSMStatus.status_log_12)
    await callback.message.answer(f'Все задания должны быть пройдены за 60 минут. Ответы принимаются в числовом виде.\nПервое задание: \n{tasks_log[1][0]}', 
                                  reply_markup=keyboard_log_tasks[0])
    #await callback.message.answer(text='Вы можете остановить тестирование.', 
                                    #reply_markup=keyboard_cancel)
    
#получение верных ответов у первых двух заданий через коллбэк
@router.callback_query(F.data == 'true', FSMStatus.status_log_12)
async def true_answer(callback: CallbackQuery, state: FSMContext):
    spare_time = users[callback.from_user.id]["finish"] - datetime.datetime.today()
    elapsed_time = datetime.datetime.today() - users[callback.from_user.id]['start']
    #проверка по времени
    await callback.message.delete()
    if datetime.datetime.now() >= users[callback.from_user.id]['finish']:
        await callback.message.answer(f"{answers['time_over']} {users[callback.from_user.id]['total_score']}") 
        await state.clear()
        await callback.answer(text='Вы можете запустить тестирование по другому предмету',
                                reply_markup=keyboard_rus
                            )
    else:
        #подсчет баллов
        #add in dict users answers of user and true
        users[callback.from_user.id][users[callback.from_user.id]['current_task']] = (tasks_log[users[callback.from_user.id]['current_task']][1], True)
        users[callback.from_user.id]['total_score'] += tasks_log[users[callback.from_user.id]['current_task']][2]
        #send next task
        users[callback.from_user.id]['current_task'] += 1
        if users[callback.from_user.id]['current_task'] < 3:
            await callback.message.answer(f'{answers["next_task"]} {users[callback.from_user.id]["current_task"]}:\n{tasks_log[users[callback.from_user.id]["current_task"]][0]}'
                                f'\nУ вас осталось: {conv_time(spare_time)}',
                                reply_markup=keyboard_log_tasks[users[callback.from_user.id]['current_task'] - 1])
        else:
            await state.set_state(FSMStatus.status_log_in)
            await callback.message.answer(f'{answers["next_task"]} {users[callback.from_user.id]["current_task"]}:\n{tasks_log[users[callback.from_user.id]["current_task"]][0]}'
                                f'\nУ вас осталось: {conv_time(spare_time)}')

        
#получение ложных ответов у первых двух заданий через коллбэк
@router.callback_query(F.data == 'false', FSMStatus.status_log_12)
async def false_answer(callback: CallbackQuery, state: FSMContext):
    spare_time = users[callback.from_user.id]["finish"] - datetime.datetime.today()
    elapsed_time = datetime.datetime.today() - users[callback.from_user.id]['start']
    users[callback.from_user.id][users[callback.from_user.id]['current_task']] = ('0', False)
    await callback.message.delete()
    #проверка по времени
    if datetime.datetime.now() >= users[callback.from_user.id]['finish']:
        await callback.message.answer(f"{answers['time_over']} {users[callback.from_user.id]['total_score']}") 
        await state.clear()
        await callback.answer(text='Вы можете запустить тестирование по другому предмету',
                                reply_markup=keyboard_rus
                            ) 
    else:
        #send next task
        users[callback.from_user.id]['current_task'] += 1
        if users[callback.from_user.id]['current_task'] < 3:
            await callback.message.answer(f'{answers["next_task"]} {users[callback.from_user.id]["current_task"]}:\n{tasks_log[users[callback.from_user.id]["current_task"]][0]}'
                        f'\nУ вас осталось: {conv_time(spare_time)}',
                        reply_markup=keyboard_log_tasks[users[callback.from_user.id]['current_task'] - 1]) 
        else:
            await state.set_state(FSMStatus.status_log_in) 
            await callback.message.answer(f'{answers["next_task"]} {users[callback.from_user.id]["current_task"]}:\n{tasks_log[users[callback.from_user.id]["current_task"]][0]}'
                        f'\nУ вас осталось: {conv_time(spare_time)}')


    
#getting text answers(3-5)
@router.message(F.text, FSMStatus.status_log_in)
async def get_answer(message: Message, state: FSMContext):
    #если время истекло
    if datetime.datetime.now() >= users[message.from_user.id]['finish']:
        await message.answer(f"{answers['time_over']} {users[message.from_user.id]['total_score']}") 
        #очистить состояния, вывести инлайн клавиатуру Другой предмет и Завершить
        await state.clear()
        await message.answer(text='Вы можете запустить тестирование по другому предмету',
                            reply_markup=keyboard_rus
                            ) 
    else:
        answer = message.text.strip().lower()
        #add in dict users answers of user and true/false
        users[message.from_user.id][users[message.from_user.id]['current_task']] = (answer, answer == tasks_log[users[message.from_user.id]['current_task']][1])
        spare_time = users[message.from_user.id]["finish"] - datetime.datetime.today()
        elapsed_time = datetime.datetime.today() - users[message.from_user.id]['start']
        if answer == tasks_log[users[message.from_user.id]['current_task']][1]:
            #начисление баллов
            users[message.from_user.id]['total_score'] += tasks_log[users[message.from_user.id]['current_task']][2]
        #check for last task
        if users[message.from_user.id]['current_task'] == list(tasks_log.keys())[-1]:
            await message.answer(f'{answers["last_task"]} {users[message.from_user.id]["total_score"]}'
                                f'\nВремя тестирования: {conv_time(elapsed_time)}')
            await state.clear()
            await message.answer(text='Вы можете запустить тестирование по другому предмету',
                                reply_markup=keyboard_rus
                                ) 
        else:
            
            #send next task
            users[message.from_user.id]['current_task'] += 1
            file_ids: list = []
            if users[message.from_user.id]['current_task'] == 4:
                image_1 = FSInputFile("school_test_bot/pictures/ABCD.png")
                result = await message.answer_photo(image_1, caption=f'{answers["next_task"]} {users[message.from_user.id]["current_task"]}:\n{tasks_log[users[message.from_user.id]["current_task"]][0]}\
                                                    \nУ вас осталось: {conv_time(spare_time)}')
                #await message.answer_photo(photo=FSInputFile('ABCD.png', 'rb'), caption=f'{answers["next_task"]} {users[message.from_user.id]["current_task"]}:\n{tasks_log[users[message.from_user.id]["current_task"]][0]}\
                                            #\nУ вас осталось: {conv_time(spare_time)}')###########
                file_ids.append(result.photo[-1].file_id)

                 
            else: 
                image_2 = FSInputFile("school_test_bot/pictures/KOD.png")
                result = await message.answer_photo(image_2, caption=f'{answers["next_task"]} {users[message.from_user.id]["current_task"]}:\n{tasks_log[users[message.from_user.id]["current_task"]][0]}\
                                \nУ вас осталось: {conv_time(spare_time)}')    
            #await message.answer(f'{answers["next_task"]} {users[message.from_user.id]["current_task"]}:\n{tasks_log[users[message.from_user.id]["current_task"]][0]}'
                                #f'\nУ вас осталось: {conv_time(spare_time)}')
            await message.answer(text='Вы можете остановить тестирование без результата.', 
                                reply_markup=keyboard_cancel)

#случайные текстовые сообщения при тестировании по Логике в заданиях 1,2          
@router.message(F.text, FSMStatus.status_log_12)
async def get_answer(message: Message): 
    await message.answer(text='Вы находитесь на стадии тестирования. \nДля получения следующего задания нажмите кнопку с ответом.')
    await message.answer(text='Вы можете остановить тестирование без результата.', 
                        reply_markup=keyboard_cancel)

         
                    

