from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

command_start = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать учиться!')],
                                            [KeyboardButton(text='О проекте CyberSaver')]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Добро пожаловать!')

emergency_exit = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Вернуться в главное меню⬅')]],
                           resize_keyboard=True,
                           input_field_placeholder='Нажмите, если хотите закончить тренировку')

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='💪УЧИТЬСЯ!!!💪')],
                                     [KeyboardButton(text='🧐Для любознательных🧐')],
                                     [KeyboardButton(text='😞Помощь😞')]],
                           resize_keyboard=True,
                           input_field_placeholder='«Изучайте прошлое, если хотите интуитивно понять будущее» -- Конфуций')

for_curious_home = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='---')],
                                     [KeyboardButton(text='Про нас (CyberSaver)')],
                                     [KeyboardButton(text='Про методики обучения')],
                                    [KeyboardButton(text='Вернуться в главное меню⬅')]],
                           resize_keyboard=True,
                           input_field_placeholder='Широкий кругозор еще никому не навредил😌')

help_home = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='---')],
                                     [KeyboardButton(text='ничего не понятно!')],
                                     [KeyboardButton(text='Вернуться в главное меню⬅')]],
                           resize_keyboard=True,
                           input_field_placeholder='Широкий кругозор еще никому не навредил😌')

command_help = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ээээ бляяя как рулить... (запутался в кнопках)')],
                                            [KeyboardButton(text='о CyberSaver'), KeyboardButton(text='разработчики')]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Выберите интересующий вас вариант....')

practice_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✅ да', callback_data='right'),
                                     InlineKeyboardButton(text='❌ Нет', callback_data='wrong')]])

after_answer = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать дальше!!!',
                                                                           callback_data='continue_practice')]])

prev_training = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать!!!',
                                                                           callback_data='continue_training'),
                                                      InlineKeyboardButton(text="напомните что делать...",
                                                                           callback_data='trainig_guide')]])

after_guide = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать!!!',
                                                                           callback_data='continue_training')]])



