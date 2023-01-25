import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import BoundFilter
from lesson24._tgapi.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
ADMIN_ID = 1040023542


def admin_filter(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        return True
    return False


class CustomFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message) -> bool:
        return message.from_user.id == ADMIN_ID


dp.filters_factory.bind(CustomFilter, event_handlers=[dp.message_handlers])

logging.basicConfig(level=logging.INFO)


# @dp.message_handler(commands=["start", "help"])
# async def welcome_message(message: types.Message):
#     await message.answer("Добро пожаловать!")

@dp.message_handler(admin_filter, commands=["start", "help"])
async def welcome_admin(message: types.Message):
    await message.answer("Добро пожаловать, Админ!")


@dp.message_handler(commands=["start", "help"])
async def welcome_user(message: types.Message):
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


async def my_filter(message: types.Message):
    # do something here
    return {'foo': 'foo', 'bar': 42}


@dp.message_handler(my_filter)
async def my_message_handler(message: types.Message, bar: int):
    await message.reply(f'bar = {bar}')


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


from aiogram.dispatcher.filters.state import State, StatesGroup


class UserForm(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name'
    age = State()  # Will be represented in storage as 'Form:age'
    gender = State()  # Will be represented in storage as 'Form:gender'


if __name__ == "__main__":
    executor.start_polling(dp)
