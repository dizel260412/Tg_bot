import requests
import json
from bs4 import BeautifulSoup


def get_first_events():
    headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / "
                      "99.0.4844.51 Safari / 537.36"
    }

    url = "https://www.championat.com/football/_russiapl/tournament/4465/calendar/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    events_live = soup.find_all("td", class_="stat-results__count _order_3")
    # with open('test.html', 'w', encoding="UTF-8") as file:
    #     file.write(r.text)

    events_dict = {}
    for event in events_live:
        url = event.find('a').get("href").strip('/')
        id_url = f'https://www.championat.com/{url}'
        id_match = url[-6:]
        text = event.find('a').get('title').strip(',')
        result = event.find('span', class_='stat-results__count-main').text.replace('\n', '').replace(' ', '')
        test = event.find_previous('a').find_previous().find_previous().find_previous().find_previous().find_previous()\
            .find_previous().find_previous().find_previous().text.replace(" ", "").replace('\n', '')
        date = test[0:10]
        time = test[11:]

        events_dict[id_match] = {
            "date": date,
            "time": time,
            "name": text,
            "result": result,
            "url": id_url
            }

    with open("events_dict1.json", "w", encoding="UTF8") as file:
        json.dump(events_dict, file, indent=4, ensure_ascii=False)


def main():
    get_first_events()


if __name__ == "__main__":
    main()
