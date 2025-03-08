from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='УЧИТЬСЯ!!!')],
                                     [KeyboardButton(text='Для любознательных')],
                                     [KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Что вы хотите сделать? Выберите нужный вариант ниже...')

command_help = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ээээ бляяя как рулить... (запутался в кнопках)')],
                                            [KeyboardButton(text='о CyberSaver'), KeyboardButton(text='разработчики')]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Выберите интересующий вас вариант....')

command_start = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Обучение')],
                                            [KeyboardButton(text='ПОГНАЛИ!!!!')],
                                             [KeyboardButton(text='О проекте'),
                                              KeyboardButton(text='Настройки')]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Добро пожаловать! Выберите продолжение...')

practice_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✅ даааа', callback_data='right'),
                                     InlineKeyboardButton(text='❌ нееееет', callback_data='wrong')]])

after_answer = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать дальше!!!',
                                                                           callback_data='continue_training')]])

prev_training = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать!!!',
                                                                           callback_data='continue_training'),
                                                      InlineKeyboardButton(text="напомните что делать...",
                                                                           callback_data='trainig_guide')]])

after_guide = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='решать!!!',
                                                                           callback_data='continue_training')]])

emergency_exit = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='В главное меню')]],
                           resize_keyboard=True,
                           input_field_placeholder='Нажмите, если хотите закончить тренировку')


