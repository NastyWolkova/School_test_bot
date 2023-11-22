from aiogram.types import (InlineKeyboardButton, Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton)

button_1 = InlineKeyboardButton(text='Русский 5 класс', callback_data='rus_pressed')
button_2 = InlineKeyboardButton(text='Логика', callback_data='log_pressed')
button_3 = InlineKeyboardButton(text='Правила', callback_data='rules_pressed')
button_4 = InlineKeyboardButton(text='Начать', callback_data='start_pressed')
button_5 = InlineKeyboardButton(text='Завершить', callback_data='cancel_pressed')

keyboard_choice = InlineKeyboardMarkup(inline_keyboard=[[button_1, button_2], [button_5]])
keyboard_start = InlineKeyboardMarkup(inline_keyboard=[[button_3, button_4], [button_5]])
keyboard_start_mini = InlineKeyboardMarkup(inline_keyboard=[[button_4, button_5]])
keyboard_cancel = InlineKeyboardMarkup(inline_keyboard=[[button_5]])
keyboard_logic = InlineKeyboardMarkup(inline_keyboard=[[button_2, button_5]])
keyboard_rus = InlineKeyboardMarkup(inline_keyboard=[[button_1, button_5]])

button_11 = InlineKeyboardButton(text='7', callback_data='false')
button_12 = InlineKeyboardButton(text='5', callback_data='false')
button_13 = InlineKeyboardButton(text='6', callback_data='true')
button_14 = InlineKeyboardButton(text='8', callback_data='false')

button_21 = InlineKeyboardButton(text='1', callback_data='false')
button_22 = InlineKeyboardButton(text='2', callback_data='true')
button_23 = InlineKeyboardButton(text='3', callback_data='false')
button_24 = InlineKeyboardButton(text='4', callback_data='false')

button_31 = InlineKeyboardButton(text='1', callback_data='false')
button_32 = InlineKeyboardButton(text='2', callback_data='true')
button_33 = InlineKeyboardButton(text='3', callback_data='false')
button_34 = InlineKeyboardButton(text='4', callback_data='false')

keyboard_1 = InlineKeyboardMarkup(inline_keyboard=[[button_11, button_12],[button_13, button_14], [button_5]])
keyboard_2 = InlineKeyboardMarkup(inline_keyboard=[[button_21, button_22],[button_23, button_24], [button_5]])
keyboard_3 = InlineKeyboardMarkup(inline_keyboard=[[button_31, button_32],[button_33, button_34], [button_5]])

spisok_keybord = [keyboard_1, keyboard_2, keyboard_3]


