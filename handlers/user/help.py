from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "ℹ️ Yordam")
async def help_handler(message: Message):
    await message.answer(
        "ℹ️ Yordam\n\n"
        "💎 UC sotib olish uchun menyudan foydalaning.\n"
        "📸 To'lov qilgandan keyin chek yuboring.\n"
        "📞 Muammo bo'lsa admin bilan bog'laning."
    )