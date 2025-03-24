from urllib.parse import uses_relative

from aiogram import Bot, Dispatcher, F, Router, types

from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from random import randint
from typing import Union

import application.keyboard as kb
import application.database.reqests as rq


router = Router()

def check_answer(task_num: int) -> bool:
	# тут будем проверять и смотреть в бд
	return True

@router.message(CommandStart())
async def cmd_start(message: Message):
	await rq.set_user(message.from_user.id)
	await message.answer('Здравствуйте!\nЭто бот CyberSaver, он поможет вам научиться защищать себя и '
						 'свои данные в глобальной сети!\nНажимайте кнопки ниже чтобы пройти обучение, начать учиться, '
						 'настроить бота или больше знать о проекте CyberSaver!',
						 reply_markup=kb.command_start)

@router.message(Command('help'))
async def cmd_help(message: Message, bot: Bot):
	sent_message = await message.answer(
		'ПОМОЩЬ!! !! \n Ты нажал на кнопку помощи!\nВыбери ниже, что ты хочешь узнать',
		reply_markup=kb.command_help)

@router.message(F.text == 'Начать учиться!')
@router.message(F.text == 'В главное меню')
async def cmd_choice(message: Message):
	await message.answer('Выбирай :/', reply_markup=kb.main)

@router.message(F.text == 'о CyberSaver')
async def cmd_about(message: Message):
	await message.answer('5 легенд слева направо: КЕЛУМ')

@router.message(F.text == 'О режимах')
async def cmd_about_mods(message: Message):
	await message.answer('На данный момент в нашем боте представлены три вида тренировки: '
						 'Аудио-, Скрин- и Текстовый режимы')
	await message.answer('В режме АУДИО вам будут отправлены голосовые сообщения, вам нужно будет определить, '
						 'настоящие они или фейковые')
	await message.answer('В режиме СКРИН, вам будет отправлен скрин диалога, нам нужно будет определить,'
						 'можно ли верить собеседнику')
	await message.answer('В режиме ТЕКСТа вам просто нужно будет прочитать небольшую предысторию, и решить, '
						 'насколько она правдива. Это поможет вам развить кругозор, зашарить за современные технологии, '
						 'чтобы не быть обманутым мошенниками, и не дать себя провести.')

@router.message(F.text == 'Обучение')
async def cmd_learn(message: Message, bot: Bot):
	sent_message = await message.answer('Добро пожаловать в киберсавер!\n Сейчас мы расскажем тебе че к чему: ....\n\n\n'
										'бот закрпеляет сообещение, поэтому если что то забудешь то оно всегда в закрепе')
	await bot.pin_chat_message(chat_id=message.chat.id, message_id=sent_message.message_id, disable_notification=True)

@router.message(F.text == 'Для любознательных')
async def cmd_curious(message: Message, bot: Bot):
	sent_message = await message.answer('ну короче тут какая нибудь прикольная инфа ахаххахах гав гав мяу мяу руэрэу гаиньг')
	sent_message = await message.answer(
		'здесть тоже будем отправлять запрос в бд, мб будут несколько разных блоков с инфой ну короче пока ниче нет',
	reply_markup=kb.main)

@router.message(F.text == 'О проекте')
async def cmd_about_project(message: Message, bot: Bot):
	sent_message = await message.answer('Проект CyberSaver реализуется студентами ММФ НГУ. Команда работает над '
										'созданием приложения, позволяющего пожилым людям тренировать свои навыки борьбы '
										'с мошенничеством в сети. CyberSaver создает интерактивный учебник-тренажер при '
										'помощи Telegram - бота. Результатом работы будет являться Telegram - бот с '
										'настроенными вкладками теории по теме, тестами, интерактивными упражнениями с '
										'элементами геймификации.')

@router.message(F.text == 'О нас')
async def cmd_about_us(message: Message, bot: Bot):
	sent_message = await message.answer('короче мы CuberSaver крутые в андрогогике вас всему научим')

@router.callback_query(F.data == "trainig_guide")
async def trainig_guide(callback: CallbackQuery):
	await callback.answer('')
	await callback.message.answer('Тут вопросы, которые моделируют реальную ситуацию. Вам надо попытаться поставить'
								  ' себя на место людей, получивших такое или похожее сообщение и продумать ваши действия'
								  'в такой ситцуации. Давайте попробуем!', reply_markup=kb.after_guide)

@router.message(F.text == 'Вернуться к выбору режима')
@router.message(F.text == 'УЧИТЬСЯ!!!')
async def cmd_practice(message: Message):
	await message.answer('НАЧИАНЕМ ТРЕНИРОВКУ!!!\n')
	await message.answer('Выбери режим тренировки! О каждом можешь узнать поподробнее, нажав на него',
						 reply_markup=kb.choose_training_type)

@router.message(F.text == 'Аудио-тренировка')
async def cmd_practice(message: Message):
	await message.answer('Вы выбрали режим аудио-тренировки!')
	await message.answer('Ты можешь начать тренировку, узнать больше о режиме или вернуться к выбору режима',
						 reply_markup=kb.audio_choosing)

@router.message(F.text == 'Имитация диалога')
async def cmd_practice(message: Message):
	await message.answer('Вы выбрали режим работы со скриншотами!')
	await message.answer('Ты можешь начать тренировку, узнать больше о режиме или вернуться к выбору режима',
						 reply_markup=kb.picture_choosing)

class PracticeStates(StatesGroup):
	waiting_answer = State()

def get_continue_button(mode):
	return kb.after_answer_pic if mode == "pic" else kb.after_answer_aud

@router.message(F.text == 'Начать тренировку!')
async def start_practice_message(message: Message, state: FSMContext):
	await message.answer("Начинаем тренировку! Сейчас будут задания, отвечайте так, как ответили бы ирл.",
						 reply_markup=kb.emergency_exit)
	await practice_handler_pic(message, state)

@router.callback_query(F.data == "continue_training_pic")
async def start_practice_callback(callback: CallbackQuery, state: FSMContext):
	await practice_handler_pic(callback.message, state)
	await callback.answer()

async def practice_handler_pic( source: Union[Message, CallbackQuery], state: FSMContext) -> None:
	task_id = randint(1, 5)
	task = await rq.get_task_pic_by_id(task_id)

	if isinstance(source, CallbackQuery):
		message = source.message
		await source.answer()
	else:
		message = source

	await state.update_data(correct_answer=task.task_answer, current_task=task, training_mode="pic" )
	await state.set_state(PracticeStates.waiting_answer)

	try:
		if task.task_picUrl and task.task_picUrl != "null":
			await message.answer_photo(
				photo=task.task_picUrl,
				caption=task.task_text,
				reply_markup=kb.practice_options
			)
		else:
			await message.answer(
				"К сожалению, не удалось загрузить изображение. "
				"Проверьте свое подключение к интернету или перезагрузите приложение телеграмм.\n "
				"Давайте продолжим тренировку в текстовом формате!"
			)
			await message.answer(f'**Задание**:\n{task.task_text}', reply_markup=kb.practice_options)
	except Exception as e:
		print(f"Ошибка pic тренировки: {e}")

@router.message(F.text == 'Начать аудио-тренировку!')
async def start_practice_message(message: Message, state: FSMContext):
	await message.answer("Начинаем тренировку! Сейчас будут задания, отвечайте так, как ответили бы ирл.",
						 reply_markup=kb.emergency_exit)
	await practice_handler_aud(message, state)

@router.callback_query(F.data == "continue_training_aud")
async def start_practice_callback(callback: CallbackQuery, state: FSMContext):
	await practice_handler_aud(callback.message, state)
	await callback.answer()

async def practice_handler_aud( source: Union[Message, CallbackQuery], state: FSMContext) -> None:
	task_id = randint(1, 5)
	task = await rq.get_task_aud_by_id(task_id)

	if isinstance(source, CallbackQuery):
		message = source.message
		await source.answer()
	else:
		message = source

	await state.update_data(correct_answer=task.task_answer, current_task=task, training_mode="aud" )
	await state.set_state(PracticeStates.waiting_answer)

	# print(f"DEBUG: task_audioLINK = {task.task_audioLINK}")
	try:
		if task.task_audioLINK and task.task_audioLINK not in ["null", ""]:
			await message.answer_audio(audio=task.task_audioLINK, caption=task.task_text,
										   reply_markup=kb.practice_options)
		else:
			await message.answer("Нет аудиофайла для этого задания. Давайте продолжим текстом.")
			await message.answer(f'**Задание**:\n{task.task_text}', reply_markup=kb.practice_options)
	except Exception as e:
		print(f"Ошибка отправки аудио: {e}")
		await message.answer("Произошла ошибка при загрузке аудио. Давайте продолжим в текстовом формате.")
		await message.answer(f'**Задание**:\n{task.task_text}', reply_markup=kb.practice_options)


@router.callback_query(StateFilter(PracticeStates.waiting_answer))
async def handle_practice_answer(callback: CallbackQuery, state: FSMContext):
	data = await state.get_data()
	task = data['current_task']
	correct_answer = task.task_answer
	training_mode = data.get("training_mode", "pic")  # По умолчанию режим "pic"
	continue_button = get_continue_button(training_mode)

	user_answer = "_____ДА_____" if callback.data == "right" else "_____НЕТ_____"
	wrong_user_answer = "_____НЕТ_____" if callback.data == "right" else "_____ДА_____"

	if callback.data == correct_answer:
		response = f'✅✅✅Ваш ответ: {user_answer}✅✅✅\nПравильно!\n\nКомментарий: {task.task_comment}\n\n'
	else:
		response = (f'❌❌❌Ваш ответ: {user_answer}❌❌❌\nНеправильно. Надо было отвечать: {wrong_user_answer} '
					f'\n\nКомментарий: {task.task_comment}\n\n')

	response += "Нажмите кнопку, чтобы продолжить тренировку в этом же режиме."

	await callback.message.answer(response, reply_markup=continue_button)
	await state.clear()
	await callback.answer()



"""----------------------------ФУНКЦИИ ОТ АДМИНА----------------------------"""

@router.message(F.photo, Command('image'))
async def photo_handler(message: Message) -> None:
	"""использовать для заполнения бд столбец task_pictures.picURL"""
	photo_data = message.photo[-1]
	print(photo_data.file_id)

# @router.message(F.audio | F.voice)
@router.message(Command('audio'))
async def audio_or_voice_handler(message: Message) -> None:
	"""использовать для заполнения бд столбец task_audio.audioLINK"""
	file_id = message.audio.file_id if message.audio else message.voice.file_id
	print(file_id)

@router.message(Command('54798_bd.info'))
async def tasks(message: Message):
	all_tasks_pic = await rq.get_tasks_pic()
	total_count = 0; pic_count = 0; aud_count = 0
	for task in all_tasks_pic: pic_count += 1

	all_tasks_pic = await rq.get_tasks_aud()
	for task in all_tasks_pic: aud_count += 1
	await message.answer(f'На данный момент бот насчитывает {total_count} заданий.\n'
						 f'Из них {pic_count} заданий с изображениями диалогов и '
						 f' {aud_count} аудио-заданий.')

@router.message(Command('54798_user.info'))
async def tasks(message: Message):
	all_users = await rq.get_users()
	count = 0
	for task in all_users: count += 1
	await message.answer(f'На данный момент бот насчитывает {count} пользователей.')