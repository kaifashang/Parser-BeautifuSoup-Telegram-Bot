from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from main import html_parser
import json

bot = Bot(token="TOKEN",
          parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Smart watch Xiaomi"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Discounted products", reply_markup=keyboard)


@dp.message_handler(Text(equals="Smart watch Xiaomi"))
async def get_discount_sneakers(message: types.Message):

    await message.answer("Please waiting...")

    html_parser()
    with open("data.json") as file:
        data = json.load(file)

    for item in data:
        photo = "".join(item[3])
        name = "".join(item[2])
        discount = "".join(item[0])
        link = "".join(item[1])

        await bot.send_photo(message.chat.id, photo, caption="<b>" + name
                             + "</b>\n<b>" + f"Скидка: {discount}"
                             + f"</b>\n<a href='{link}'>Ссылка на сайт</a>",
                             parse_mode="html")


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
