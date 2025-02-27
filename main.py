import asyncio

from aiogram import Bot, Dispatcher
from application.handlers import router

async def main():
	bot = Bot(token="7894875925:AAHgpxBiuFlIfIkFmTLTMKRM1w2EH-NcZKs")
	dp = Dispatcher()
	dp.include_router(router)
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())