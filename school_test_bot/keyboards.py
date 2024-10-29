from aiogram.types import (InlineKeyboardButton, Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton)

#кнопки общего назначения
button_1 = InlineKeyboardButton(text='Русский язык 5 класс', callback_data='rus_pressed')
button_2 = InlineKeyboardButton(text='Логика', callback_data='log_pressed')
button_3 = InlineKeyboardButton(text='Правила', callback_data='rules_pressed')
button_4 = InlineKeyboardButton(text='Начать', callback_data='start_pressed')
button_5 = InlineKeyboardButton(text='Завершить', callback_data='cancel_pressed')

#клавы общего назначения
keyboard_choice = InlineKeyboardMarkup(inline_keyboard=[[button_1, button_2], [button_5]])
keyboard_start = InlineKeyboardMarkup(inline_keyboard=[[button_3, button_4], [button_5]])
keyboard_start_mini = InlineKeyboardMarkup(inline_keyboard=[[button_4, button_5]])
keyboard_cancel = InlineKeyboardMarkup(inline_keyboard=[[button_5]])
keyboard_logic = InlineKeyboardMarkup(inline_keyboard=[[button_2, button_5]])
keyboard_rus = InlineKeyboardMarkup(inline_keyboard=[[button_1, button_5]])

#кнопки-ответы для РЯ
#for big questsion number 1
button_11_1 = InlineKeyboardButton(text='не имеет', callback_data='true')
button_11_2 = InlineKeyboardButton(text='нулевую', callback_data='false')
button_12_1 = InlineKeyboardButton(text='ЛИСИ-', callback_data='false')
button_12_2 = InlineKeyboardButton(text='ЛИС-', callback_data='true')
button_12_3 = InlineKeyboardButton(text='ЛИСИЙ-', callback_data='false')
button_13_1 = InlineKeyboardButton(text='не имеет', callback_data='false')
button_13_2 = InlineKeyboardButton(text='-С-', callback_data='false')
button_13_3 = InlineKeyboardButton(text='-ИЙ-', callback_data='true')
button_14_1 = InlineKeyboardButton(text='нулевое', callback_data='true')
button_14_2 = InlineKeyboardButton(text='-ИЙ', callback_data='false')
button_14_3 = InlineKeyboardButton(text='-Й', callback_data='false')

button_21 = InlineKeyboardButton(text='5', callback_data='false')
button_22 = InlineKeyboardButton(text='все', callback_data='false')
button_23 = InlineKeyboardButton(text='1, 4', callback_data='true')
button_24 = InlineKeyboardButton(text='2, 3, 5', callback_data='false')
button_25 = InlineKeyboardButton(text='1, 3, 4', callback_data='false')

button_31 = InlineKeyboardButton(text='1, 2, 3', callback_data='false')
button_32 = InlineKeyboardButton(text='1, 3, 4', callback_data='true')
button_33 = InlineKeyboardButton(text='4', callback_data='false')
button_34 = InlineKeyboardButton(text='2', callback_data='false')
button_35 = InlineKeyboardButton(text='нет верного ответа', callback_data='false')

button_41 = InlineKeyboardButton(text='1, 2, 3', callback_data='false')
button_42 = InlineKeyboardButton(text='2, 3', callback_data='false')
button_43 = InlineKeyboardButton(text='1', callback_data='false')
button_44 = InlineKeyboardButton(text='4', callback_data='false')
button_45 = InlineKeyboardButton(text='все', callback_data='false')
button_46 = InlineKeyboardButton(text='2, 3, 4', callback_data='true')

button_51 = InlineKeyboardButton(text='Все', callback_data='false')
button_52 = InlineKeyboardButton(text='1, 2', callback_data='true')
button_53 = InlineKeyboardButton(text='1, 2, 3', callback_data='false')
button_54 = InlineKeyboardButton(text='1 и 2', callback_data='false')
button_55 = InlineKeyboardButton(text='3, 4', callback_data='false')
button_56 = InlineKeyboardButton(text='Все, кроме 1', callback_data='false')

button_61 = InlineKeyboardButton(text='мороз', callback_data='false')
button_62 = InlineKeyboardButton(text='всадить', callback_data='false')
button_63 = InlineKeyboardButton(text='сбежать', callback_data='false')
button_64 = InlineKeyboardButton(text='восемь', callback_data='true')

button_71 = InlineKeyboardButton(text='2, 4', callback_data='false')
button_72 = InlineKeyboardButton(text='2, 3, 4', callback_data='true')
button_73 = InlineKeyboardButton(text='2, 3', callback_data='false')
button_74 = InlineKeyboardButton(text='все верные, кроме 3', callback_data='false')
button_75 = InlineKeyboardButton(text='все верные', callback_data='false')

button_81 = InlineKeyboardButton(text='1, 2', callback_data='false')
button_82 = InlineKeyboardButton(text='3, 4', callback_data='false')
button_83 = InlineKeyboardButton(text='1, 3, 4', callback_data='false')
button_84 = InlineKeyboardButton(text='1', callback_data='true')
button_85 = InlineKeyboardButton(text='во всех', callback_data='false')


#клавы длы каждого вопроса РЯ

# big russian question number 1
keyboard_11 = InlineKeyboardMarkup(inline_keyboard=[[button_11_1, button_11_2], [button_5]]) #приставка
keyboard_12 = InlineKeyboardMarkup(inline_keyboard=[[button_12_1, button_12_2], [button_12_3, button_5]]) #корень
keyboard_13 = InlineKeyboardMarkup(inline_keyboard=[[button_13_1, button_13_2], [button_13_3, button_5]]) #суффикс
keyboard_14 = InlineKeyboardMarkup(inline_keyboard=[[button_14_1, button_14_2], [button_14_3, button_5]]) #окончание

keyboard_2 = InlineKeyboardMarkup(inline_keyboard=[[button_21], [button_22], [button_23], [button_24], [button_25], [button_5]])
keyboard_3 = InlineKeyboardMarkup(inline_keyboard=[[button_31], [button_32], [button_33], [button_34], [button_35], [button_5]])
keyboard_4 = InlineKeyboardMarkup(inline_keyboard=[[button_41], [button_42],[button_43], [button_44], [button_45], [button_46], [button_5]])
keyboard_5 = InlineKeyboardMarkup(inline_keyboard=[[button_51, button_52],[button_53, button_54], [button_55, button_56], [button_5]])
keyboard_5 = InlineKeyboardMarkup(inline_keyboard=[[button_51, button_52],[button_53, button_54], [button_55, button_56], [button_5]])
keyboard_6 = InlineKeyboardMarkup(inline_keyboard=[[button_61, button_62],[button_63, button_64], [button_5]])
keyboard_7 = InlineKeyboardMarkup(inline_keyboard=[[button_71, button_72],[button_73, button_74], [button_75, button_5]])
keyboard_8 = InlineKeyboardMarkup(inline_keyboard=[[button_81, button_82],[button_83, button_84], [button_85, button_5]])

keybord_rus_tasks = ([keyboard_11, keyboard_12, keyboard_13, keyboard_14], keyboard_2, keyboard_3, keyboard_4, keyboard_5, keyboard_6, keyboard_7, keyboard_8)
#spisok_keybord = [keyboard_1, keyboard_2, keyboard_3]

#кнопки-ответы на логику
button_1_1 = InlineKeyboardButton(text='А-лжец, В-шпион, С-рыцарь', callback_data='false')
button_1_2 = InlineKeyboardButton(text='А-лжец, С-шпион, В-рыцарь', callback_data='false')
button_1_3 = InlineKeyboardButton(text='С-лжец, А-шпион, В-рыцарь', callback_data='false')
button_1_4 = InlineKeyboardButton(text='В-лжец, А-шпион, С-рыцарь', callback_data='false')
button_1_5 = InlineKeyboardButton(text='С-лжец, В-шпион, А-рыцарь', callback_data='true')
button_1_6 = InlineKeyboardButton(text='В-лжец, С-шпион, А-рыцарь', callback_data='false')

button_2_1 = InlineKeyboardButton(text='Иванов, Сидоров, Титов', callback_data='false')
button_2_2 = InlineKeyboardButton(text='Иванов, Титов, Сидоров', callback_data='false')
button_2_3 = InlineKeyboardButton(text='Титов, Сидоров, Иванов', callback_data='true')
button_2_4 = InlineKeyboardButton(text='Титов, Иванов, Сидоров', callback_data='false')
button_2_5 = InlineKeyboardButton(text='Сидоров, Титов, Иванов', callback_data='false')
button_2_6 = InlineKeyboardButton(text='Сидоров, Иванов, Титов', callback_data='false')


keyboard_log_1 = InlineKeyboardMarkup(inline_keyboard=[[button_1_1], [button_1_2], [button_1_3], [button_1_4], [button_1_5], [button_1_6], [button_5]])
keyboard_log_2 = InlineKeyboardMarkup(inline_keyboard=[[button_2_1], [button_2_2], [button_2_3], [button_2_4], [button_2_5], [button_2_6], [button_5]])

keyboard_log_tasks = (keyboard_log_1, keyboard_log_2)