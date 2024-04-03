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
    sens = State()

@dp.message(F.text.in_({'/start','/hi'}))
async def command_start_handler(message: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text="/msg")],
        [types.KeyboardButton(text="/mon")],
        [types.KeyboardButton(text="/input")],
        [types.KeyboardButton(text="/sens")]
    ]
    global keyboard 
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("usage", reply_markup=keyboard)
    from ui import Ui_Dialog
    await addhistory(message.from_user.id,message.text,message.from_user.username)
@dp.message(F.text.in_({'/mon'}))
async def commands_handler(message: types.Message) -> None:
    await message.answer("monitor:")
    await addhistory(message.from_user.id,message.text,message.from_user.username)
    await bot.send_photo(chat_id=message.chat.id,photo=types.FSInputFile(scrt()))

#----------message
@dp.message(F.text.in_({'/msg'}))
async def commands_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.msgtext)
    await message.answer("enter text")
    await addhistory(message.from_user.id,message.text,message.from_user.username)
@dp.message(Form.msgtext)
async def process_text(message: types.Message, state: FSMContext) -> None:
    await state.update_data(msgtext=message.text)
    multiprocessing.Process(target=msgwindow,args=(message.text,)).start()
    await addhistory(message.from_user.id,message.text,message.from_user.username)
    await message.answer("sent")
    await state.clear()
#----------
    

#----------input
@dp.message(F.text.in_({'/input'}))
async def commands_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.inputText)
    await message.answer("enter text",reply_markup=ReplyKeyboardRemove())
    await addhistory(message.from_user.id,message.text,message.from_user.username)

@dp.message(Form.inputText)
async def process_text(message: types.Message, state: FSMContext) -> None:
    await state.update_data(inputText=message.text)
    await state.set_state(Form.getans)
    multiprocessing.Process(target=msgwindowAns,args=(message.chat.id,message.text)).start()
    await addhistory(message.from_user.id,message.text,message.from_user.username)
    await state.clear()
#----------
    

#----------image click
    
@dp.message(F.text.in_({'/sens'}))

async def commands_handler(message: types.Message, state: FSMContext) -> None:
    kb = [
        [types.KeyboardButton(text="exit sens mode")],
        [types.KeyboardButton(text="double click")],
        [types.KeyboardButton(text="rgb mon")],
        [types.KeyboardButton(text="gray mon")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await state.set_state(Form.sens)
    await bot.send_photo(chat_id=message.chat.id,photo=types.FSInputFile(sendingGrayScale()),reply_markup=keyboard)
    await addhistory(message.from_user.id,message.text,message.from_user.username)

@dp.message(Form.sens)
async def process_text(message: types.Message, state: FSMContext) -> None:
    if message.text == 'exit sens mode':
        await state.clear()
        kb = [
        [types.KeyboardButton(text="/msg")],
        [types.KeyboardButton(text="/mon")],
        [types.KeyboardButton(text="/input")],
        [types.KeyboardButton(text="/sens")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("sens mode off", reply_markup=keyboard)
        await addhistory(message.from_user.id,message.text,message.from_user.username)
    elif message.text == 'rgb mon':
        await bot.send_photo(chat_id=message.chat.id,photo=types.FSInputFile(scrt()))
    elif message.text == 'gray mon':
        await bot.send_photo(chat_id=message.chat.id,photo=types.FSInputFile(sendingGrayScale()))
    elif message.text == 'double click':
        doubleClick()
        await bot.send_photo(chat_id=message.chat.id,photo=types.FSInputFile(sendingGrayScale()))
    else:

        await message.answer("monitor:")
        await message.bot.download(file=message.photo[-1].file_id, destination="files/gotDot.png")
        clickByPhoto()
        await bot.send_photo(chat_id=message.chat.id,photo=types.FSInputFile(sendingGrayScale()))
    
#----------
@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
        if message.text:
            await addhistory(message.from_user.id,message.text,message.from_user.username)
    except TypeError:
        await message.answer("NA")

async def main(TOKEN) -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    
def starter(TOKEN):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(TOKEN))
    
