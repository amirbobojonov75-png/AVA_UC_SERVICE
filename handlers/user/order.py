from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.order import OrderState
from config import CARD_NUMBER, CARD_OWNER

router = Router()


@router.message(OrderState.waiting_pubg_id)
async def get_pubg_id(message: Message, state: FSMContext):

    data = await state.get_data()

    await state.update_data(
        pubg_id=message.text
    )

    await message.answer(
        "✅ Buyurtma:\n\n"
        f"💎 UC: {data['uc']}\n"
        f"💰 Narx: {data['price']}\n"
        f"🆔 PUBG ID: {message.text}\n\n"
        "💳 To'lov ma'lumotlari:\n\n"
        f"Karta: {CARD_NUMBER}\n"
        f"Egasi: {CARD_OWNER}\n\n"
        "📸 To'lov qilgandan keyin chek rasmini yuboring."
    )

    await state.set_state(OrderState.waiting_check)