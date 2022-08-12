import asyncio
import json
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token, user_id, headers, url_dict
from get_first_news import get_first_news

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все новости", "Последние 5 новостей", "Свежие новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Лента новостей", reply_markup=keyboard)

    @dp.message_handler(Text(equals="Все новости"))
    async def get_all_news(message: types.Message):
        with open(get_first_news.dict_name, encoding="UTF8") as file:
            news_dict = json.load(file)

        for k, v in sorted(news_dict.items()):
            news = f"{hbold(v['data'])}\n" \
                   f"{hlink(v['title'], v['url'])}"

            await message.answer(news)


if __name__ == '__main__':
    start('start')