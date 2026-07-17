import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from handlers import routers
from database.models import create_tables


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)

    await create_tables()

    print("✅ Bot ishga tushdi.")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())