import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import BOT_TOKEN
from handlers import start, menu, expenses, journal, settings, balance

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        menu.router,
        expenses.router,
        balance.router,
        journal.router,
        settings.router,
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    while True:
        try:
            asyncio.run(main())
        except Exception as e:
            print(f"Xatolik: {e}. Bot qayta ishga tushyapti.")
