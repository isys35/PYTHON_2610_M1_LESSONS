from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor, markdown
from aiogram.types import ParseMode

from lesson25._example_bot.config import TOKEN

bot = Bot(token=TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    name = State()
    age = State()
    gender = State()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await UserState.name.set()
    await message.reply("Добро пожаловать, как тебя зовут?")


@dp.message_handler(state=UserState.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text

    await UserState.next()
    await message.reply("Сколько тебе лет?")


@dp.message_handler(lambda message: not message.text.isdigit(), state=UserState.age)
async def process_age_invalid(message: types.Message):
    await message.reply("Возраст должен быть числом!")


@dp.message_handler(lambda message: message.text.isdigit(), state=UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    await UserState.next()
    await state.update_data(age=int(message.text))

    markup = types.ReplyKeyboardMarkup()
    markup.add("Муж", "Жен")
    await message.reply("Укажите пол?", reply_markup=markup)


@dp.message_handler(lambda message: message.text not in ['Муж', 'Жен'], state=UserState.gender)
async def process_gender_invalid(message: types.Message):
    await message.reply("Пол введён неверно!")


@dp.message_handler(lambda message: message.text in ['Муж', 'Жен'], state=UserState.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    markup = types.ReplyKeyboardRemove()

    async with state.proxy() as data:
        await bot.send_message(
            message.chat.id,
            markdown.text(
                markdown.text("Приятно познакомится!", markdown.bold(data["name"])),
                markdown.text("Возраст:", markdown.code(data["age"])),
                markdown.text("Пол:", data["gender"]),
                sep="\n"
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN
        )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
