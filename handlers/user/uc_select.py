from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from states.order import OrderState

router = Router()


uc_prices = {
    "uc_60": ("60 UC", "12 000 so'm"),
    "uc_120": ("120 UC", "25 000 so'm"),
    "uc_180": ("180 UC", "39 000 so'm"),
    "uc_325": ("325 UC", "59 000 so'm"),
    "uc_385": ("385 UC", "73 000 so'm"),
    "uc_660": ("660 UC", "117 000 so'm"),
    "uc_720": ("720 UC", "130 000 so'm"),
    "uc_985": ("985 UC", "177 000 so'm"),
    "uc_1320": ("1320 UC", "234 000 so'm"),
    "uc_1800": ("1800 UC", "300 000 so'm"),
    "uc_2120": ("2120 UC", "360 000 so'm"),
    "uc_3850": ("3850 UC", "570 000 so'm"),
    "uc_5170": ("5170 UC", "760 000 so'm"),
    "uc_5650": ("5650 UC", "870 000 so'm"),
    "uc_8100": ("8100 UC", "1 130 000 so'm"),
}


@router.callback_query(lambda call: call.data in uc_prices)
async def uc_select_handler(call: CallbackQuery, state: FSMContext):

    uc, price = uc_prices[call.data]

    await state.update_data(
        uc=uc,
        price=price
    )

    await call.message.answer(
        f"✅ {uc}\n"
        f"💰 Narxi: {price}\n\n"
        "🆔 PUBG ID raqamingizni yuboring:"
    )

    await state.set_state(OrderState.waiting_pubg_id)

    await call.answer()