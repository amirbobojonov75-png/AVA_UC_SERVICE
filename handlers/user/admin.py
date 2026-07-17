from aiogram import Router
from aiogram.types import Message

from keyboards.inline import admin_button

router = Router()


@router.message(lambda message: message.text == "📞 Admin")
async def admin_handler(message: Message):
    await message.answer(
        "📞 Admin\n\n"
        "Bog'lanish uchun tugmani bosing:",
        reply_markup=admin_button
    )