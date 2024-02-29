import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import *
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import TOKEN
from util import *
from aiogram.methods import SendPhoto


dp = Dispatcher()

@dp.message(F.text.in_({'/start','/hi'}))
async def command_start_handler(message: Message) -> None:
    kb = [
        [types.KeyboardButton(text="/msg")],
        [types.KeyboardButton(text="/mon")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("usage", reply_markup=keyboard)

@dp.message(F.text.in_({'/mon'}))
async def commands_handler(message: types.Message) -> None:
    await message.answer("monitor:")
    await bot.send_photo(chat_id=message.chat.id,photo=types.FSInputFile(scrt()))



@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())