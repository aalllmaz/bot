from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command("about"))
async def about(message: types.Message):
    text = "Данного бота написала Александра Кудрина, студентка третьего курса РГГУ, в качестве своей экзаменационной" \
           " работы.\n\nЗадача бота очень проста, он предоставляет возможность пройти несколько психологических опросов. \n\nС" \
           " обратной связью можете написать мне в telegem @aalllmaz"
    await message.answer(text=text)
