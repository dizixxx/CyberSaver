from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='УЧИТЬСЯ!!!')],
                                     [KeyboardButton(text='Для любознательных')],
                                     [KeyboardButton(text='Об обучении')]],
                           resize_keyboard=True,
                           input_field_placeholder='Что вы хотите сделать? Выберите нужный вариант ниже...')

command_help = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ээээ бляяя как рулить... (запутался в кнопках)')],
                                            [KeyboardButton(text='о CyberSaver'), KeyboardButton(text='разработчики')]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Выберите интересующий вас вариант....')

command_start = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Обучение')],
                                            [KeyboardButton(text='Начать учиться!')],
                                             [KeyboardButton(text='О проекте'),
                                              KeyboardButton(text='Настройки')]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Добро пожаловать!')

choose_training_type = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Аудио-тренировка',
                                                                     callback_data="training_aud")],
                                     [KeyboardButton(text='Имитация диалога',
                                                     callback_data="training_pic")],
                                     [KeyboardButton(text='Текстовая тренировка (не нажимать, не работает)',
                                                     callback_data="training_text")],
                                     [KeyboardButton(text='О режимах'), KeyboardButton(text='В главное меню')]],
                           resize_keyboard=True,
                           input_field_placeholder='Какой вид тренировки?')

audio_choosing = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать аудио-тренировку!',
                                                               callback_data="training_aud")],
                                             [KeyboardButton(text='О режиме'),
                                              KeyboardButton(text='Вернуться к выбору режима',
                                                             callback_data="УЧИТЬСЯ!!!")]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Выбирайте...')

picture_choosing = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать тренировку!',
                                                               callback_data="training_aud")],
                                             [KeyboardButton(text='О режиме'),
                                              KeyboardButton(text='Вернуться к выбору режима',
                                                             callback_data="УЧИТЬСЯ!!!")]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Выбирайте...')

practice_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✅ да', callback_data='right'),
                                     InlineKeyboardButton(text='❌ Нет', callback_data='wrong')]])

after_answer_pic = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать дальше!!!',
                                                                           callback_data='continue_training_pic')]])
after_answer_aud = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать дальше!!!',
                                                                           callback_data='continue_training_aud')]])

prev_training = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать!!!',
                                                                           callback_data='continue_training'),
                                                      InlineKeyboardButton(text="напомните что делать...",
                                                                           callback_data='trainig_guide')]])

after_guide = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать!!!',
                                                                           callback_data='continue_training')]])

emergency_exit = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Вернуться к выбору режима')]],
                           resize_keyboard=True,
                           input_field_placeholder='Нажмите, если хотите закончить тренировку')


