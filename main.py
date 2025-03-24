import asyncio

from aiogram import Bot, Dispatcher

from application.handlers import router
from application.database.models import async_main

async def main():
	await async_main()
	bot = Bot(token="7894875925:AAHgpxBiuFlIfIkFmTLTMKRM1w2EH-NcZKs")
	dp = Dispatcher()
	dp.include_router(router)
	await dp.start_polling(bot)

if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("Бот выключен")