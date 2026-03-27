import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from app.handlers import router

from app.handlers import time_now


async def main():
    session = AiohttpSession(proxy="")
    bot = Bot(token="", session=session)
    
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print(f"{time_now} | [ON] Бот успешно включен")
        asyncio.run(main())

    except (Exception, asyncio.CancelledError) as e:
        print(f"{time_now} | [OFF] Бот отключен: {e}")