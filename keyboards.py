from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

start_button = [
        [KeyboardButton(text="Узнать погоду.")]
    ]
start_button = ReplyKeyboardMarkup(keyboard=start_button, resize_keyboard=True)

menu_forecast = [
    [InlineKeyboardButton(text='В данный момент.', callback_data='current_day'),
     InlineKeyboardButton(text='На весь день.', callback_data='all_day')],
    [InlineKeyboardButton(text='На три дня.', callback_data='three_days'),
     InlineKeyboardButton(text='В главное меню.', callback_data='cancel')]
]
menu_forecast = InlineKeyboardMarkup(inline_keyboard=menu_forecast)

menu_geo = [
    [InlineKeyboardButton(text='Определить местоположение.', callback_data='get_geo')]
]
menu_geo = InlineKeyboardMarkup(inline_keyboard=menu_geo)

back_button = [
    [InlineKeyboardButton(text='В главное меню.', callback_data='cancel')]
]
back_button = InlineKeyboardMarkup(inline_keyboard=back_button)