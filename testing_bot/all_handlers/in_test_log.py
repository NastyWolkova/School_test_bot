from aiogram import Router, F
from fsmstatus import FSMStatus
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import or_f
from lexicon.lexicon import tasks_log, answers, users 
import datetime
from keyboards import keyboard_cancel, keyboard_rus
from functions import conv_time



router: Router = Router()

#ТЕСТИРОВАНИЕ, получение первого задания (и смена статуса юзера)
@router.callback_query(F.data == 'start_pressed', or_f(FSMStatus.status_log, FSMStatus.status_rus))
async def process_button_4_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    dt1 = datetime.datetime.today()
    dt2 = dt1 + datetime.timedelta(minutes=3)
    users[callback.from_user.id]['current_task'] = 1
    users[callback.from_user.id]['start'] = dt1
    users[callback.from_user.id]['finish'] = dt2
    await state.set_state(FSMStatus.status_log_in)
    await callback.message.answer(f'Все задания должны быть пройдены за 3 минуты. Ответы принимаются в числовом виде.\nПервое задание: \n{tasks_log[1][0]}')
    await callback.message.answer(text='Вы можете остановить тестирование.', 
                                    reply_markup=keyboard_cancel)

#for logic tasks
@router.message(lambda x: x.text.isdigit(), FSMStatus.status_log_in)
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
        answer = message.text
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
            await message.answer(f'{answers["next_task"]} {users[message.from_user.id]["current_task"]}:\n{tasks_log[users[message.from_user.id]["current_task"]][0]}'
                                f'\nУ вас осталось: {conv_time(spare_time)}')
            await message.answer(text='Вы можете остановить тестирование без результата.', 
                                reply_markup=keyboard_cancel)

#случайные текстовые сообщения при тестировании по Логике            
@router.message(F.text, FSMStatus.status_log_in)
async def get_answer(message: Message):     
    await message.answer(text='Вы находитесь в стадии тестирования. \nОтветы на задания по Логике принимаются в виде числа.')
    await message.answer(text='Вы можете остановить тестирование без результата.', 
                        reply_markup=keyboard_cancel)       
                    

