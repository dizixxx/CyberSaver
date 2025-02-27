from urllib.parse import uses_relative

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import application.keyboard as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
	await message.answer('Привет!\nЭто бот CyberSaver, чтобы помочь тебе научиться защищать себя и '
						 'свои данные в глобальной сети!\nЖми кнопки ниже чтобы узнать больше!',
						 reply_markup=kb.command_start)

@router.message(Command('help'))
async def cmd_help(message: Message, bot: Bot):
	sent_message = await message.answer(
        'ПОМОЩЬ!! !! \n Ты нажал на кнопку помощи!\nВыбери ниже, что ты хочешь узнать',
        reply_markup=kb.command_help)

@router.message(F.text == 'ПОГНАЛИ!!!!')
async def cmd_choice(message: Message):
	await message.answer('Выбирай :/', reply_markup=kb.main)

@router.message(F.text == 'о CyberSaver')
async def cmd_about(message: Message):
	await message.answer('5 легенд слева направо: КЕЛУМ')

@router.message(F.text == 'Обучение.')
async def cmd_learn(message: Message, bot: Bot):
	sent_message = await message.answer('Доброг пожаловать в киберсавер!\n Сейчас мы расскажем тебе че к чему: ....\n\n\n'
										'бот закрпеляет сообещение, поэтому если что то забудешь то оно всегда в закрепе')
	await bot.pin_chat_message(chat_id=message.chat.id, message_id=sent_message.message_id, disable_notification=True)