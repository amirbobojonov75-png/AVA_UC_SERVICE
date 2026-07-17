from aiogram import Router
from aiogram.types import Message

from database.queries import get_orders

router = Router()


@router.message(lambda message: message.text == "📦 Buyurtmalarim")
async def my_orders(message: Message):

    orders = get_orders(message.from_user.id)

    if not orders:
        await message.answer("📦 Sizda hali buyurtmalar yo'q.")
        return

    text = "📦 Buyurtmalarim:\n\n"

    for order in orders:
        text += (
            f"🆔 Buyurtma #{order[0]}\n"
            f"💎 {order[1]}\n"
            f"💰 {order[2]}\n"
            f"🎮 PUBG ID: {order[3]}\n"
            f"📌 Holati: {order[4]}\n\n"
        )

    await message.answer(text)