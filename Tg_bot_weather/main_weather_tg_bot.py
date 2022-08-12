import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я скажу тебе погоду!")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        datetime.datetime.now().strftime('%H:%M %d-%m-%Y')
        region = data["sys"]["country"]
        city = data["name"]
        temp = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода)"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).time()
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).time()

        await message.reply(f"Прогноз погоды: {datetime.datetime.now().strftime('%H:%M %d-%m-%Y')} \n"
                            f"Погода в городе: {region} / {city}\n"
                            f"Температура: {round(temp)} °C {wd}\n"
                            f"Влажность воздуха: {humidity} %\n"
                            f"Атмосферное давление: {pressure} мм рт. ст\n"
                            f"Ветер: {wind} M/c\n"
                            f"Восход: {sunrise} \U00002600\n"
                            f"Закат: {sunset} \U0001F319 \n"
                            )

    except:
        await message.reply("\U00002620 Проверьте название города! \U00002620")


if __name__ == "__main__":
    executor.start_polling(dp)
