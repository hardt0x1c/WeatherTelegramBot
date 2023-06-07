import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Text
from aiogram.types import ReplyKeyboardRemove
from config import bot_token
import keyboards as kb
import messages as msg
import Weather

logging.basicConfig(level=logging.INFO)
bot = Bot(bot_token)
dp = Dispatcher()
storage = MemoryStorage()


class States(StatesGroup):
    request_city = State()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(msg.greet, reply_markup=kb.start_button)


@dp.message(Text('Узнать погоду.'))
async def get_city(message: types.Message, state: FSMContext):
    await state.set_state(States.request_city)
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(msg.get_geo_text, reply_markup=ReplyKeyboardRemove())
    await message.answer(msg.get_geo_text2, reply_markup=kb.back_button)


@dp.message(States.request_city)
async def get_forecast(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(msg.get_forecast, reply_markup=kb.menu_forecast)


@dp.callback_query(Text('current_day'), States.request_city)
async def get_current_day(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    city = data.get('city')
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer(Weather.start_weather_current(city), reply_markup=kb.menu_forecast)


@dp.callback_query(Text('all_day'), States.request_city)
async def get_all_day(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    city = data.get('city')
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer(Weather.start_weather_forecast(city), reply_markup=kb.menu_forecast)


@dp.callback_query(Text('three_days'), States.request_city)
async def get_three_day(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    city = data.get('city')
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer(Weather.start_weather_three_days(city), reply_markup=kb.menu_forecast)


@dp.callback_query(Text('cancel'))
async def cancel_handler(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('Главное меню:', reply_markup=kb.start_button)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
