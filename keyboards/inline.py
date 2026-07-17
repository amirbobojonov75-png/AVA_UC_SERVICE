from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


admin_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="👤 Admin bilan bog'lanish",
                url="https://t.me/avaaaaaaaa27"
            )
        ]
    ]
)


uc_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="60 UC", callback_data="uc_60"),
            InlineKeyboardButton(text="120 UC", callback_data="uc_120")
        ],
        [
            InlineKeyboardButton(text="180 UC", callback_data="uc_180"),
            InlineKeyboardButton(text="325 UC", callback_data="uc_325")
        ],
        [
            InlineKeyboardButton(text="385 UC", callback_data="uc_385"),
            InlineKeyboardButton(text="660 UC", callback_data="uc_660")
        ],
        [
            InlineKeyboardButton(text="720 UC", callback_data="uc_720"),
            InlineKeyboardButton(text="985 UC", callback_data="uc_985")
        ],
        [
            InlineKeyboardButton(text="1320 UC", callback_data="uc_1320"),
            InlineKeyboardButton(text="1800 UC", callback_data="uc_1800")
        ],
        [
            InlineKeyboardButton(text="2120 UC", callback_data="uc_2120"),
            InlineKeyboardButton(text="3850 UC", callback_data="uc_3850")
        ],
        [
            InlineKeyboardButton(text="5170 UC", callback_data="uc_5170"),
            InlineKeyboardButton(text="5650 UC", callback_data="uc_5650")
        ],
        [
            InlineKeyboardButton(text="8100 UC", callback_data="uc_8100")
        ]
    ]
)