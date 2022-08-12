import requests
import json
from bs4 import BeautifulSoup


def get_first_events():
    headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / "
                      "99.0.4844.51 Safari / 537.36"
    }

    url = "https://www.championat.com/stat/football/#2022-04-01"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    events_live = soup.find_all('li', class_="seo-results__item")
    with open('test_tooday.html', 'w', encoding="UTF-8") as file:
        file.write(r.text)
    #
    # events_dict = {}
    # for event in events_live:
    #     url = event.find('a').get("href").strip("/")
    #     if url[-7] == "/":
    #         id_title = url[-6:]
    #     else:
    #         id_title = url[-7:]
    #     id_url = f'https://www.championat.com/{url}'
    #     time = event.find("span", class_="seo-results__item-date").text
    #     title = event.find('a').text
    #     status = event.find("span", class_="seo-results__item-status").text
    #     # print(f'{id_url} | {id_title} | {time} | {title} | {status}')
    #
    #
    #     events_dict[id_title] = {
    #         "time": time,
    #         "name": title,
    #         "status": status,
    #         "url": id_url
    #         }
    #
    # with open("events_dict2.json", "w", encoding="UTF8") as file:
    #     json.dump(events_dict, file, indent=4, ensure_ascii=False)


def main():
    get_first_events()


if __name__ == "__main__":
    main()
