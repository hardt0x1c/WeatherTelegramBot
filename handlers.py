import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import key, access_token, bot_token
import keyboards
from messages import *


logging.basicConfig(level=logging.INFO)
bot = Bot(bot_token)
dp = Dispatcher()
storage = MemoryStorage()


