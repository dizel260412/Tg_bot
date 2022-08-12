import datetime
from config import open_weather_token
from pprint import pprint
import requests


def get_weather(city, open_weather_token):
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
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

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

        print(f"Прогноз погоды: {datetime.datetime.now().strftime('%H:%M %d-%m-%Y')} \n"
              f"Погода в городе: {region} / {city}\n"
              f"Температура: {temp} °C {wd}\n"
              f"Влажность воздуха: {humidity} %\n"
              f"Атмосферное давление: {pressure} мм рт. ст\n"
              f"Ветер: {wind} M/c\n"
              f"Восход: {sunrise}\n"
              f"Закат: {sunset}\n"

              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города!")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
