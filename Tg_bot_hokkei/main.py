import json
import requests
from bs4 import BeautifulSoup


def get_first_events():
    headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / "
                      "99.0.4844.51 Safari / 537.36"
    }

    url = "https://www.sport-express.ru/hockey/L/khl/2021-2022/calendar/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    events_data = soup.find_all("div", class_="sp-CalendarMatchesByDay-day")
    events = soup.find_all("td", class_="sp-CalendarMatch__col--teamsNames")

    events_dict = {}
    for event in events_data:
        data = event.find("h2", class_="sp-CalendarMatchesByDay__dayTitle").text.strip()
        time = event.find("td", class_="sp-CalendarMatch__col--date").text.strip()
        name = event.find("td", class_="sp-CalendarMatch__matchStage").text.strip()
        command = event.find()
        events_dict[data] = {
            "data": data,
            "time": time,
            "name": name,

        }

    with open("events_dict1.json", "w", encoding="UTF8") as file:
        json.dump(events_dict, file, indent=4, ensure_ascii=False)


def main():
    get_first_events()


if __name__ == "__main__":
    main()
