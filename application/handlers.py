from urllib.parse import uses_relative

from aiogram import Bot, Dispatcher, F, Router, types

from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
import random

from sqlalchemy.util import await_only

import application.keyboard as kb
import application.database.reqests as rq
from application.database.models import GosuslugiTopic, SberTopic

router = Router()

"""-------------------------------------------------ФУНКЦИИ ОТ АДМИНА------------------------------------------------"""
"""------------------------------------------------------------------------------------------------------------------"""

@router.message(F.photo, Command('image'))
async def photo_handler(message: Message) -> None:
	"""использовать для заполнения бд столбец task_pictures.picURL"""
	photo_data = message.photo[-1]
	print(photo_data.file_id)

@router.message(F.audio | F.voice)
# @router.message(Command('audio'))
async def audio_or_voice_handler(message: Message) -> None:
	"""использовать для заполнения бд столбец task_audio.audioLINK"""
	file_id = message.audio.file_id if message.audio else message.voice.file_id
	print(file_id)

@router.message(Command('54798_user.info'))
async def tasks(message: Message):
	all_users = await rq.get_users()
	count = 0
	for task in all_users: count += 1
	await message.answer(f'На данный момент бот насчитывает {count} пользователей.')

@router.message(Command('help'))
async def cmd_help(message: Message, bot: Bot):
	sent_message = await message.answer(
		'ПОМОЩЬ!! !! \n Ты нажал на кнопку помощи!\nВыбери ниже, что ты хочешь узнать',
		reply_markup=kb.command_help)

"""------------------------------------------------------------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------------------------------"""

@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
	await rq.set_user(message.from_user.id)
	await message.answer('Здравствуйте! Добро пожалость в бот CyberSaver!\nЭтот бот - разработка студентов НГУ, '
						 'помогающая борьбе с преступностью в Интернете!\n'
						 'В настоящее время Интернет наполнен огромным количеством мошенников, которые используют '
						 'любые современные методы для того, чтобы обманывать людей и присваивать себе их имущество и данные.\n'
						 'Мы считаем, что любой человек может научиться правильно защищаться в Сети, а в случае беды'
						 'уметь правильно реагировать на сложивуюся ситцацию. Для этого и создан наш проект!\n')
	sent_message = await message.answer('Этот проект представляет собой интерактивный тренажер, имеющий три типа заданий:'
						 'Аудио-, Скрин- и Текстовый режимы. Сейчас расскажем попордробнее:\n'
						 'В режме АУДИО вам будут отправлены голосовые сообщения, вам нужно будет определить, настоящие они или фейковые.\n'
						 'В режиме СКРИН, вам будет отправлен скрин диалога, нам нужно будет определить,'
						 'можно ли верить собеседнику.\n В режиме ТЕКСТа вам просто нужно будет прочитать небольшую предысторию, и решить, '
						 'насколько она правдива. Это поможет вам развить кругозор, зашарить за современные технологии'
						 ', чтобы не быть обманутым мошенниками, и не дать себя провести!\n'
						 'Кстати,'
						 'бот сам закрепляет сообщение, поэтому если что-то будет непонятно, нажмите на плашку в верхней части экрана!')
	await bot.pin_chat_message(chat_id=message.chat.id, message_id=sent_message.message_id, disable_notification=True)
	await message.answer('Звучит сложновато, однако это лишь на первый взгляд! Давайте начнем первую тренировку!',
						 reply_markup = kb.command_start)

@router.message(F.text == 'О проекте CyberSaver')
async def cmd_about_project(message: Message):
	sent_message = await message.answer('Проект CyberSaver реализуется студентами ММФ НГУ. Команда работает над '
										'созданием приложения, позволяющего людям серебряного возраста тренировать свои '
										'навыки борьбы с мошенничеством в сети. CyberSaver создает интерактивный учебник-тренажер'
										'на платформе Telegram. Результатом работы будет являться Telegram - бот с '
										'настроенными вкладками теории по теме, тестами, интерактивными упражнениями  несокльких типов'
										'с элементами геймификации.')

@router.message(F.text == 'Начать учиться!')
@router.message(F.text == 'Вернуться в главное меню⬅')
async def cmd_about_project(message: Message):
	await message.answer('Замечательно!\nЗдесь вы можете начать отрабатывать практические навыки,'
										'прочитать интересные истории и лайфхаки, а так же обратиться за помощью!',
										reply_markup=kb.main)

@router.message(F.text == '🧐Для любознательных🧐')
async def cmd_curious(message: Message):
	await message.answer('В этом разделе вы можете узнать о том, как защищаться от самых современных видов'
										'Интернет-мошенничества, послушать истории реальных людей, обманутых преступниками,'
										'прочитать про интересные приемы и многое другое!', reply_markup=kb.for_curious_home)

@router.message(F.text == '😞Помощь😞')
async def cmd_curious(message: Message):
	await message.answer('чек закреп хз\nЕсли есть вопросы по боту, пишите @Dj_arbuzzzzzzz',
						 reply_markup=kb.for_curious_home)


"""--------------------trainig parth--------------------------------"""

topics = ["sber", "gosuslugi"]

@router.message(F.text == '💪УЧИТЬСЯ!!!💪')
async def start_practice_callback(message: Message, state: FSMContext):
	await message.answer('Начинаем тренировку!', reply_markup=kb.emergency_exit)
	current_topic = random.choice(topics)
	await load_questions_for_topic(state, current_topic)
	await send_question(message, state)


async def load_questions_for_topic(state: FSMContext, topic: str):
	if topic == "sber":
		topic_tasks = await rq.get_sber_topic_tasks()
	else:
		topic_tasks = await rq.get_gosuslugi_topic_tasks()

	task_list = list(topic_tasks)
	await state.update_data(current_topic=topic, question_count=0, topic_questions=task_list)

async def send_question(message: Message, state: FSMContext):
	data = await state.get_data()
	question_count = data.get("question_count", 0)
	topic_questions = data.get("topic_questions", [])
	current_topic = data.get("current_topic")
	last_message_id = data.get("last_message_id")

	search_class = {
		"gosuslugi": [GosuslugiTopic, "ОПАСНОСТЬ С ГОСУСЛУГ!!"],
		"sber": [SberTopic, "ВЗЛОМ ОНЛАЙН КОШЕЛЬКА!!!"],
	}

	if question_count >= 5 or not topic_questions:
		await message.answer('-----------------КОНЕЦ ТОПИКА-----------------------')
		await message.answer('Замечательно! Вы улучшили свою безопасность на 5 вопросов!'
							 'У мошенников почти не осталось шансов против вас!')
		new_topic = random.choice([t for t in topics if t != current_topic])
		await load_questions_for_topic(state, new_topic)
		data = await state.get_data()
		topic_questions = data.get("topic_questions", [])
		current_topic = data.get("current_topic")
		question_count = 0
		await message.answer(f'Давайте порешаем на новую тему! Например, как вам идея: {search_class[current_topic][1]}')

	if not topic_questions:
		await message.answer("В данной категории пока нет заданий, попробуйте позже.")
		return

	task = random.choice(topic_questions)
	await state.update_data(correct_answer=task.task_answer, right_comment=task.task_right_comment,
							wrong_comment=task.task_wrong_comment, question_count=question_count + 1)

	if last_message_id:
		try:
			await message.bot.edit_message_reply_markup(chat_id=message.chat.id,
														message_id=last_message_id,
														reply_markup=None)
		except Exception as e:
			print(f"Ошибка при удалении inline-кнопок: {e}")

	answer_options = await rq.get_answer_options(task.task_id, search_class[current_topic][0])

	buttons = [
		InlineKeyboardButton(text=option, callback_data=f"answer_{index}")
		for index, option in enumerate(answer_options)
	]

	n = len(buttons)
	if n == 2:
		rows = [buttons[:2]]
	elif n == 3:
		rows = [buttons[:2], buttons[2:]]
	elif n == 4:
		rows = [buttons[:2], buttons[2:4]]
	elif n == 5:
		rows = [buttons[:2], buttons[2:4], buttons[4:]]
	elif n == 6:
		rows = [buttons[:2], buttons[2:4], buttons[4:]]
	else:
		rows = [[btn] for btn in buttons]

	keyboard = InlineKeyboardMarkup(inline_keyboard=rows)


	try:
		if task.task_link and task.task_link != "null":
			if task.task_type == "pic":
				sent_message = await message.answer_photo(task.task_link, caption=task.task_text, reply_markup=keyboard)
			elif task.task_type == "aud":
				sent_message = await message.answer_voice(task.task_link, caption=task.task_text, reply_markup=keyboard)
			else:
				sent_message = await message.answer(task.keyboard, reply_markup=keyboard)

		else:
			await message.answer(
				"К сожалению, не удалось загрузить изображение. "
				"Проверьте свое подключение к интернету или перезагрузите приложение телеграмм.\n "
				"Давайте продолжим тренировку в текстовом формате!"
			)
			sent_message = await message.answer(f'**Задание**:\n{task.task_text}', reply_markup=keyboard)

		await state.update_data(last_message_id=sent_message.message_id)

	except Exception as e:
		print(f'ошибка при отправке файла {task.task_type}: {e}\n'
			  f'{task.task_id} || {task.task_text} || {task.task_link}')

@router.callback_query(F.data.startswith("answer_"))
async def process_answer(callback: CallbackQuery, state: FSMContext):
	await callback.answer()
	data = await state.get_data()
	correct_answer = data.get("correct_answer")
	right_comment = data.get("right_comment")
	wrong_comment = data.get("wrong_comment")

	callback_data = callback.data
	answer_index = int(callback_data.split("_")[1])

	if correct_answer == answer_index:
		response = f"✅ Правильно!\n\nКомментарий:\n{right_comment}"
	else:
		response = f"❌ Неправильно.\n\nКомментарий:\n{wrong_comment}"

	await callback.message.answer(response)
	await send_question(callback.message, state)

@router.callback_query(F.data == "continue_practice")
async def continue_practice(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await send_question(callback.message, state)
