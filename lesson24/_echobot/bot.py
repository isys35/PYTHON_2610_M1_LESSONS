import logging

from aiogram import Bot, Dispatcher, executor, types

from lesson24._tgapi.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start", "help"])
async def welcome_message(message: types.Message):
    await message.answer("Добро пожаловать!")


def auf_filter(message: types.Message):
    if message.text.lower().startswith("ауф"):
        return True
    return False


@dp.message_handler(auf_filter)
async def auf(message: types.Message):
    await message.answer("Ауф")


@dp.message_handler(lambda message: message.text == 'Как дела?')
async def send_answer(message: types.Message):
    await message.answer("Нормально, у тебя как?")


# from random import choice
#
#
# @router.message(content_types="text")
# async def my_text_handler(message: types.Message):
#     phrases = [
#         "Привет! Отлично выглядишь :)",
#         "Хэллоу, сегодня будет отличный день!",
#         "Здравствуй)) улыбнись :)"
#     ]
#     if message.from_user.id in (111, 777):
#         await message.answer(choice(phrases))
#     else:
#         await message.answer("Я с тобой не разговариваю!")


if __name__ == "__main__":
    executor.start_polling(dp)
