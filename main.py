import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import *
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from util import *
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendPhoto
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import multiprocessing

dp = Dispatcher()

class Form(StatesGroup):
    inputText = State()
    getans = State()
    msgtext = State()

@dp.message(F.text.in_({'/start','/hi'}))
async def command_start_handler(message: Message) -> None:
    kb = [
        [types.KeyboardButton(text="/msg")],
        [types.KeyboardButton(text="/mon")],
        [types.KeyboardButton(text="/input")]
    ]
    global keyboard 
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("usage", reply_markup=keyboard)

@dp.message(F.text.in_({'/mon'}))
async def commands_handler(message: types.Message) -> None:
    await message.answer("monitor:")
    await bot.send_photo(chat_id=message.chat.id,photo=types.FSInputFile(scrt()))


#----------message
@dp.message(F.text.in_({'/msg'}))
async def commands_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.msgtext)
    await message.answer("enter text")

@dp.message(Form.msgtext)
async def process_text(message: types.Message, state: FSMContext) -> None:
    await state.update_data(msgtext=message.text)
    multiprocessing.Process(target=msgwindow,args=(message.text,)).start()
    await message.answer("sent")
    await state.clear()
    

#----------
    

#----------input
@dp.message(F.text.in_({'/input'}))
async def commands_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.inputText)
    await message.answer("enter text",reply_markup=ReplyKeyboardRemove())


@dp.message(Form.inputText)
async def process_text(message: types.Message, state: FSMContext) -> None:
    await state.update_data(inputText=message.text)
    await state.set_state(Form.getans)
    multiprocessing.Process(target=msgwindowAns,args=(message.chat.id,message.text)).start()
    await state.clear()

#----------
    


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("NA")


async def main(TOKEN) -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    

def starter(TOKEN):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(TOKEN))
    


def show_text(text):
    msgwindow(text)
if __name__ =="__main__":
    starter()

    
