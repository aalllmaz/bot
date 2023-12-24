from aiogram import executor

from loader import dp
from tests import burnout, personality
from bot_commands import help, start, start_testing, about, unidentified_text
from bot_commands.type_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
