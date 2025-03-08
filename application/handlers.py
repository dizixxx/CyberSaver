from urllib.parse import uses_relative

from aiogram import Bot, Dispatcher, F, Router, types

from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from random import choice

import application.keyboard as kb

router = Router()

def check_answer(task_num: int) -> bool:
	# тут будем проверять и смотреть в бд
	return True

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
@router.message(F.text == 'В главное меню')
async def cmd_choice(message: Message):
	await message.answer('Выбирай :/', reply_markup=kb.main)

@router.message(F.text == 'о CyberSaver')
async def cmd_about(message: Message):
	await message.answer('5 легенд слева направо: КЕЛУМ')

@router.message(F.text == 'Обучение')
async def cmd_learn(message: Message, bot: Bot):
	sent_message = await message.answer('Добро пожаловать в киберсавер!\n Сейчас мы расскажем тебе че к чему: ....\n\n\n'
										'бот закрпеляет сообещение, поэтому если что то забудешь то оно всегда в закрепе')
	await bot.pin_chat_message(chat_id=message.chat.id, message_id=sent_message.message_id, disable_notification=True)

@router.message(F.text == 'Для любознательных')
async def cmd_learn(message: Message, bot: Bot):
	sent_message = await message.answer('ну короче тут какая нибудь прикольная инфа ахаххахах гав гав мяу мяу руэрэу гаиньг')
	sent_message = await message.answer(
		'здесть тоже будем отправлять запрос в бд, мб будут несколько разных блоков с инфой ну короче пока ниче нет',
	reply_markup=kb.main)

@router.message(F.text == 'О проекте')
async def cmd_learn(message: Message, bot: Bot):
	sent_message = await message.answer('Проект CyberSaver реализуется студентами ММФ НГУ. Команда работает над '
										'созданием приложения, позволяющего пожилым людям тренировать свои навыки борьбы '
										'с мошенничеством в сети. CyberSaver создает интерактивный учебник-тренажер при '
										'помощи Telegram - бота. Результатом работы будет являться Telegram - бот с '
										'настроенными вкладками теории по теме, тестами, интерактивными упражнениями с '
										'элементами геймификации.')

@router.message(F.text == 'О нас')
async def cmd_learn(message: Message, bot: Bot):
	sent_message = await message.answer('короче мы CuberSaver крутые в андрогогике вас всему научим')

# @router.message(F.text == 'блок с практикой')
# async def cmd_practice(message: Message):
# 	await message.answer('мама: скинь сто тысяч. Скинешь?', reply_markup=kb.practice_options)
# 	answer = check_answer(1)
#
# @router.callback_query()
# async def inline_button_handler(callback: CallbackQuery) -> str:
# 	## тут будем смотреть в бд и оттуда брать ответ по номеру задания
# 	bd = "right"
# 	await callback.answer('Вы ответили на вопрос!')
# 	if callback.data == bd:
# 		await callback.message.answer('Правильно!!!!!! мамуля это святое и ей отказыать нельзя!\n'
# 									  'переходи к следющему вопросу!', reply_markup=kb.after_answer)
# 	else:
# 		await callback.message.answer('нет. \nчек пояснение: мамуля это святое и ей отказыать нельзя!\n '
# 									  'переходи к некст вопросу!', reply_markup=kb.after_answer)

@router.callback_query(F.data == "trainig_guide")
async def trainigguide(callback: CallbackQuery):
	await callback.answer('')
	await callback.message.answer('что то', reply_markup=kb.after_guide)

qlist = ["мама: скинь 100 тысяч. Скинешь?", "папа: скажи пароль от карты и я куплю тебе мороженое. Скажешь?",
		 "скинь 100 руб на номер 89137176220"]

@router.message(F.text == 'УЧИТЬСЯ!!!')
async def cmd_practice(message: Message):
	random_question = choice(qlist)
	await message.answer('НАЧИАНЕМ ТРЕНИРОВКУ!!!\n', reply_markup=kb.emergency_exit)
	await message.answer('Сейчас будут вопросики. отвечай да или нет\n'
						 'Ты можешь закончить тренировку нажав на кнопку ниже или после своего ответа',
						 reply_markup=kb.prev_training)

@router.callback_query(F.data == "right")
@router.callback_query(F.data == "wrong")
async def inline_button_handler(callback: CallbackQuery):
	bd = "wrong" # ищем в бд правильный ответ. Пока что бд = нет
	await callback.answer('')
	if F.data == "right":
		users_ans = "✅ Да"
	else:
		users_ans = "❌ Нет"
	if callback.data == bd:
		await callback.message.answer(f'ваш ответ: {users_ans}\nПравильно! \n\nтут будет комментарий\n\n'
									  'Переходи к следующему вопросу или выбери выход в главное меню.',
									  reply_markup=kb.after_answer)
		"""-------------- тут будет ячейка бд: код - формулировка - ответ - пояснение ---------------------"""
	else:
		await callback.message.answer(f'ваш ответ: {users_ans}\nНеправильно.\n\nтут будет комментарий\n\nПереходи '
									  f'к следующему вопросу или выбери выход в главное меню.',
									  reply_markup=kb.after_answer)

@router.callback_query(F.data == "continue_training")
async def continue_practice(callback: CallbackQuery):
	await callback.answer('')
	random_question = choice(qlist)
	await callback.message.answer(f'{random_question}', reply_markup=kb.practice_options)