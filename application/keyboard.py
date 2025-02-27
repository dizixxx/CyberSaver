from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='блок с теорией'),
                                     KeyboardButton(text='блок с практикой')],
                                     [KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Что вы хотите сделать? Выберите нужный вариант ниже...')

command_help = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ээээ бляяя как рулить... (запутался в кнопках)')],
                                            [KeyboardButton(text='о CyberSaver'), KeyboardButton(text='разработчики')]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Выберите интересующий вас вариант....')

command_start = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Обучение.')],
                                            [KeyboardButton(text='ПОГНАЛИ!!!!')],
                                             [KeyboardButton(text='правила пользования'),
                                              KeyboardButton(text='Настройки')]],
                                  resize_keyboard=True,
                                  input_field_placeholder='Добро пожаловать! Выберите продолжение...')

move_between_history = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬅️️', callback_data='back'),
                                     InlineKeyboardButton(text='➡️', callback_data='forward')]])

