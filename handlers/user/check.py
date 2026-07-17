from database.queries import add_order
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from states.order import OrderState
from config import ADMIN_ID

router = Router()


def admin_buttons(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎁 UC yuborildi",
callback_data=f"success_{user_id}"
                ),
                InlineKeyboardButton(
                    text="❌ Rad etish",
                    callback_data=f"reject_{user_id}"
                )
            ]
        ]
    )


@router.message(OrderState.waiting_check)
async def get_check(message: Message, state: FSMContext):

    if not message.photo:
        await message.answer(
            "📸 Chekni rasm ko'rinishida yuboring."
        )
        return

    data = await state.get_data()
    add_order(
    user_id=message.from_user.id,
    username=message.from_user.username,
    uc=data["uc"],
    price=data["price"],
    pubg_id=data["pubg_id"]
)

    await message.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=message.photo[-1].file_id,
        caption=(
            "🆕 Yangi buyurtma\n\n"
            f"👤 Mijoz: {message.from_user.full_name}\n"
            f"🆔 Telegram ID: {message.from_user.id}\n"
            f"💎 UC: {data['uc']}\n"
            f"💰 Narx: {data['price']}\n"
            f"🎮 PUBG ID: {data['pubg_id']}"
        ),
        reply_markup=admin_buttons(message.from_user.id)
    )

    await message.answer(
        "✅ Chek qabul qilindi.\n"
        "Admin tekshiradi."
    )

    await state.clear()