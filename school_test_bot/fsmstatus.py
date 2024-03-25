from aiogram.fsm.state import State, StatesGroup


class FSMStatus(StatesGroup):
    status_log = State()        # Состояние выбранного предмета вне тестирования
    status_rus =State()         # Состояние выбранного предмета вне 
    status_log_in = State()
    status_log_12 = State()        
    status_rus_in =State()
    status_rus_1 = State()



