import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.bot.handlers import router
from aiogram.fsm.storage.memory import MemoryStorage

async def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT")

    bot = Bot(token=token)
    dp = Dispatcher(storage=MemoryStorage()) 
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())