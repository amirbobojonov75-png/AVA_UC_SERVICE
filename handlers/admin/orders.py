from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


def order_buttons(user_id):
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


@router.callback_query(lambda call: call.data.startswith("success_"))
async def success_order(call: CallbackQuery):
    user_id = int(call.data.split("_")[1])

    await call.bot.send_message(
        user_id,
        "🎉 Buyurtmangiz muvaffaqiyatli bajarildi!\n\n"
        "💎 UC hisobingizga muvaffaqiyatli yuborildi.\n\n"
        "AVA UC SERVICE'ni tanlaganingiz uchun rahmat! ❤️"
    )

    await call.message.edit_caption(
        caption=call.message.caption +
        "\n\n🟢 Holat: UC yuborildi"
    )

    await call.answer("Mijozga xabar yuborildi.")


@router.callback_query(lambda call: call.data.startswith("reject_"))
async def reject_order(call: CallbackQuery):
    user_id = int(call.data.split("_")[1])

    await call.bot.send_message(
        user_id,
        "❌ Buyurtmangiz rad etildi.\n"
        "Admin bilan bog'laning."
    )

    await call.message.edit_caption(
        caption=call.message.caption +
        "\n\n🔴 Holat: Rad etildi"
    )

    await call.answer()