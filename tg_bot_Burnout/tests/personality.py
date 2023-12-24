from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram import types


@dp.message_handler(Command("on_start_personality_test"))
async def on_start_test(message: types.Message, state: FSMContext):
        await message.answer("Упас, данный тест ещё не готов")
        await state.finish()
