from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💎 UC sotib olish")
        ],
        [
            KeyboardButton(text="📦 Buyurtmalarim"),
            KeyboardButton(text="👤 Profil")
        ],
        [
            KeyboardButton(text="📞 Admin"),
            KeyboardButton(text="ℹ️ Yordam")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Kerakli bo'limni tanlang..."
)