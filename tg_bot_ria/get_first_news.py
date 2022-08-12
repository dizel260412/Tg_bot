import json
import requests
from bs4 import BeautifulSoup


def get_first_news(headers, url, dict_name):
    headers = headers

    url = url
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    news = soup.find_all("div", class_="list-item")

    dict_name = f"news_dict_{dict_name}.json"
    news_dict = {}
    for item in news:
        title = item.find('div', 'list-item__content').text
        url = item.find('a').get('href')
        id = url.split('-')[1][:-5]
        time_ = item.find('div', class_="list-item__date").text

        news_dict[id] = {
            'time': time_,
            'title': title,
            'URL': url
        }

        with open(dict_name, "w", encoding="UTF8") as file:
            json.dump(news_dict, file, indent=4, ensure_ascii=False)
