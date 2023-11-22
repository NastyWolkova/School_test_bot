from aiogram import Router, F
from fsmstatus import FSMStatus
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import or_f
from lexicon.lexicon import tasks_log, tasks_rus, answers, users 
import datetime, time
from keyboards import keyboard_cancel, spisok_keybord, keyboard_logic
from functions import conv_time



router: Router = Router()

#ТЕСТИРОВАНИЕ, получение первого задания (и смена статуса юзера)
@router.callback_query(F.data == 'start_pressed', FSMStatus.status_rus)
async def process_button_4_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    dt1 = datetime.datetime.today()
    dt2 = dt1 + datetime.timedelta(minutes=3)
    users[callback.from_user.id]['current_task'] = 1
    users[callback.from_user.id]['start'] = dt1
    users[callback.from_user.id]['finish'] = dt2
    await state.set_state(FSMStatus.status_rus_in)
    print(type(list(tasks_rus.keys())[-1]), type(users[callback.from_user.id]['current_task']))
    await callback.message.answer(f'У вас 3 минуты на решение всех заданий.\nПервое задание: \n{tasks_rus[1][0]}',
                                    reply_markup=spisok_keybord[0])
    
#получение верных ответов 
@router.callback_query(F.data == 'true', FSMStatus.status_rus_in)
async def true_answer(callback: CallbackQuery, state: FSMContext):
    spare_time = users[callback.from_user.id]["finish"] - datetime.datetime.today()
    elapsed_time = datetime.datetime.today() - users[callback.from_user.id]['start']
    #проверка по времени
    if datetime.datetime.now() >= users[callback.from_user.id]['finish']:
        await callback.message.answer(f"{answers['time_over']} {users[callback.from_user.id]['total_score']}") 
        await state.clear()
        await callback.answer(text='Вы можете запустить тестирование по другому предмету',
                             reply_markup=keyboard_logic
                          )
    else:
        #подсчет баллов
        #add in dict users answers of user and true
        users[callback.from_user.id][users[callback.from_user.id]['current_task']] = (tasks_rus[users[callback.from_user.id]['current_task']][1], True)
        users[callback.from_user.id]['total_score'] += tasks_rus[users[callback.from_user.id]['current_task']][2]
        #check for last task
        if users[callback.from_user.id]['current_task'] == list(tasks_rus.keys())[-1]:
            await callback.message.answer(f'{answers["last_task"]} {users[callback.from_user.id]["total_score"]}'
                                f'\nВремя тестирования: {conv_time(elapsed_time)}')
            await state.clear()
            await callback.message.answer(text='Вы можете запустить тестирование по другому предмету',
                             reply_markup=keyboard_logic
                          ) 
        else:
            #send next task
            users[callback.from_user.id]['current_task'] += 1
            await callback.message.answer(f'{answers["next_task"]} {users[callback.from_user.id]["current_task"]}:\n{tasks_rus[users[callback.from_user.id]["current_task"]][0]}'
                                f'\nУ вас осталось: {conv_time(spare_time)}',
                                reply_markup=spisok_keybord[users[callback.from_user.id]['current_task'] - 1])

#получение ложных ответов 
@router.callback_query(F.data == 'false', FSMStatus.status_rus_in)
async def false_answer(callback: CallbackQuery, state: FSMContext):
    spare_time = users[callback.from_user.id]["finish"] - datetime.datetime.today()
    elapsed_time = datetime.datetime.today() - users[callback.from_user.id]['start']
    users[callback.from_user.id][users[callback.from_user.id]['current_task']] = ('0', False)
    #проверка по времени
    if datetime.datetime.now() >= users[callback.from_user.id]['finish']:
        await callback.message.answer(f"{answers['time_over']} {users[callback.from_user.id]['total_score']}") 
        await state.clear()
        await callback.answer(text='Вы можете запустить тестирование по другому предмету',
                             reply_markup=keyboard_logic
                          ) 
    else:
        #check for last task
        if users[callback.from_user.id]['current_task'] == list(tasks_rus.keys())[-1]:
            await callback.message.answer(f'{answers["last_task"]} {users[callback.from_user.id]["total_score"]}'
                                f'\nВремя тестирования: {conv_time(elapsed_time)}')
            await state.clear()
            await callback.message.answer(text='Вы можете запустить тестирование по другому предмету',
                             reply_markup=keyboard_logic
                          ) 
        else:
            #send next task
            users[callback.from_user.id]['current_task'] += 1
            await callback.message.answer(f'{answers["next_task"]} {users[callback.from_user.id]["current_task"]}:\n{tasks_rus[users[callback.from_user.id]["current_task"]][0]}'
                                f'\nУ вас осталось: {conv_time(spare_time)}',
                                reply_markup=spisok_keybord[users[callback.from_user.id]['current_task'] - 1])



#случайный текст при тестировании
@router.message(FSMStatus.status_rus_in)
async def get_text(message: Message):
    await message.answer(text='Вы проходите тестирование по русскому языку. Для отправки ответа воспользуйтесь кнопками под заданием.')    

#случайный текст до запуска теста
@router.message(FSMStatus.status_rus)
async def get_text(message: Message):
    await message.answer(text='Вы выбрали тестирование по Русскому языку. Запустите или завершите его, воспользовавшись кнопками из сообщения.')    