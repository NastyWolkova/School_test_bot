from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import Command, CommandStart, StateFilter, or_f
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from keyboards import keyboard_choice, keyboard_start, keyboard_cancel, keyboard_start_mini
from fsmstatus import FSMStatus
from lexicon.lexicon import users
import datetime

router: Router = Router()


#команда старт незарегистрированному юзеру(без состояния)
@router.message(CommandStart(), StateFilter(default_state))
async def command_start(message: Message):
    # await message.delete()
    # await message.answer(
    #     text='удаление завершить',
    #     reply_markup=ReplyKeyboardMarkup()
    # )
    await message.answer(
        text='Выберите предмет',
        reply_markup=keyboard_choice
    )


#команда старт в состоянии уже выбранного предмета(status_log|status_rus)
@router.message(CommandStart(), or_f(FSMStatus.status_log, FSMStatus.status_rus))
async def command_start(message: Message):
    await message.answer(
        text='Вы уже выбрали предмет. Запустите или отмените тестирование.',
        reply_markup=keyboard_start
    )

#команда старт в состоянии ТЕСТИРОВАНИЯ 
@router.message(CommandStart(), or_f(FSMStatus.status_rus_in, FSMStatus.status_log_in))
async def command_start(message: Message):
    await message.answer(
        text='Вы проходите тестирование. Вы можете завершить его без результата.',
        reply_markup=keyboard_cancel  
    )

#щтмена выбора и всех статусов
@router.callback_query(F.data == 'cancel_pressed')
async def process_button_5_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.clear()
    await callback.message.answer(
                            text='Вы вышли из тестирования. Если вы решите начать заново, воспользуйтесь командой /start'
                          )

#команда хелп для всех состояний в меню бота
@router.message(Command(commands=['help']))
async def command_start(message: Message):
    await message.answer(
       text='С помощью этого бота вы можете пройти тестирование по двум предметам: русскому языку и логике. Для начала испытания выберите предмет, начав с команды /start'
        )
 

#выбор предмета РЯ и занесение в словарь user_id со сменой статуса на Status_rus
@router.callback_query(F.data == 'rus_pressed')
async def process_button_1_press(callback: CallbackQuery, state: FSMContext):
    users[callback.from_user.id] = {'subject': 'rus',
                                    'current_task': 0,
                                    'total_score': 0,
                                    'start': datetime,
                                    'finish': datetime,
                                     1: tuple(),
                                     2: tuple(),
                                     3: tuple()
                                    }
    await callback.message.delete()
    await state.set_state(FSMStatus.status_rus)
    await callback.message.answer(
        text='Вы выбрали тестирование \nпо Русскому языку: \nначните его или узнайте правила',
        reply_markup=keyboard_start
    )
    
#выбор предмета Логики и занесение в словарь user_id со сменой статуса на Status_log
@router.callback_query(F.data == 'log_pressed')
async def process_button_2_press(callback: CallbackQuery, state: FSMContext):
    users[callback.from_user.id] = {'subject': 'log',
                                    'current_task': 0,
                                    'total_score': 0,
                                     1: tuple(),
                                     2: tuple(),
                                     3: tuple(),
                                     4: tuple(),
                                     5: tuple()
                                    }
    await callback.message.delete()
    await state.set_state(FSMStatus.status_log)
    await callback.message.answer(
        text='Вы выбрали тестирование \nпо Логике: \nначните его или узнайте правила',
        reply_markup=keyboard_start
    )

#кнопка Правила при выбранном предмете
@router.callback_query(F.data == 'rules_pressed')
async def process_button_3_press(callback: CallbackQuery):
    await callback.message.delete()
    if users[callback.from_user.id]['subject'] == 'rus':
        await callback.message.answer(
            text='Здесь будут указаны правила для русского',
            reply_markup=keyboard_start_mini
        )
    else:
        await callback.message.answer(
            text='Здесь будут указаны правила для логики',
            reply_markup=keyboard_start_mini
        )

#случайные текстовые сообщения вне состояний            
@router.message(F.text, StateFilter(default_state))
async def get_text(message: Message):     
    await message.delete()
    await message.answer(
        text='Для прохождения тестирования выберите предмет',
        reply_markup=keyboard_choice
    )  

#случайные текстовые при выбранной Логике            
@router.message(F.text, FSMStatus.status_log)
async def get_text(message: Message):     
    await message.delete()
    await message.answer(
        text='Вы выбрали тестирование по Логике. \nЗапустите тестирование',
        reply_markup=keyboard_start_mini
    )                   

#случайные текстовые при выбранном РусЯз            
@router.message(F.text, FSMStatus.status_rus)
async def get_text(message: Message):     
    await message.delete()
    await message.answer(
        text='Вы выбрали тестирование по Русскому языку. \nЗапустите тестирование',
        reply_markup=keyboard_start_mini
    )    