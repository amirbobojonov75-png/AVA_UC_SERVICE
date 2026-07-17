from aiogram import Router
from aiogram.types import Message

from keyboards.inline import uc_menu

router = Router()


@router.message(lambda message: message.text == "💎 UC sotib olish")
async def buy_uc_handler(message: Message):
    await message.answer(
        "💎 UC paketini tanlang:",
        reply_markup=uc_menu
    )