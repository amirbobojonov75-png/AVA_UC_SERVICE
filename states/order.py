from aiogram.fsm.state import State, StatesGroup


class OrderState(StatesGroup):
    waiting_pubg_id = State()
    waiting_check = State()