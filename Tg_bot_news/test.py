import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import undetected_chromedriver
import time

driver = undetected_chromedriver.Chrome()
driver.get("https://yandex.ru/news")
r = requests.get(url=driver)

req = requests.get(driver)
src = req.text
with open("index_text.html", "w", encoding="UTF-8") as file:
    file.write(src)

# def get_first_news():
#     headers = {
#         "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 99.0.4844.51 Safari / 537.36"
#     }
#
#     url = "https://yandex.ru/news"
#     r = requests.get(url=url, headers=headers)
#
#     req = requests.get(url, headers=headers)
#     src = req.text
#
#
#     # soup = BeautifulSoup(r.text, "lxml")
#     # news = soup.find_all("div", class_="mg-card mg-card_flexible-single mg-card_media-fixed-height mg-card_type_image mg-grid__item")
#     with open("index_text.html", "w", encoding="UTF-8") as file:
#         file.write(src)
#     news_dict = {}
#     for new in news:
#         title = new.find("div", class_="rubric").text.strip()
#         descriptions = new.find("span", class_="text").text.strip()
#         new_url = f'https://news.sportbox.ru{new.find("a", class_="").get("href")}'
#         new_data_time = new.find("span", class_="date").text.strip()
#
#         id_url = new_url.split("/")[-1]
#         if id_url[8:17][0] == "_":
#             id_url = id_url[9:18]
#         else:
#             id_url = id_url[8:17]
#
#         # print(f"{title} | {descriptions} | {new_url} | {new_data_time}")
#
#         news_dict[id_url] = {
#             "data": new_data_time,
#             "title": title,
#             "descriptions": descriptions,
#             "url": new_url
#         }
#     with open("news_dict.json", "w", encoding="UTF8") as file:
#         json.dump(news_dict, file, indent=4, ensure_ascii=False)
#
#
# def check_news_update():
#     with open("news_dict.json", encoding="UTF8") as file:
#         news_dict = json.load(file)
#
#     headers = {
#         "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 99.0.4844.51 Safari / 537.36"
#     }
#
#     url = "https://news.sportbox.ru/Vidy_sporta/Futbol"
#     r = requests.get(url=url, headers=headers)
#
#     soup = BeautifulSoup(r.text, "lxml")
#     news = soup.find_all("div", class_="_Sportbox_Spb2015_Components_TeazerBlock_TeazerBlock")
#
#     frefh_news = {}
#     for new_list in news:
#         new_url = f'https://news.sportbox.ru{new_list.find("a", class_="").get("href")}'
#         id_url = new_url.split("/")[-1]
#         if id_url[8:17][0] == "_":
#             id_url = id_url[9:18]
#         else:
#             id_url = id_url[8:17]
#
#         if id_url in news_dict:
#             continue
#         else:
#             title = new_list.find("div", class_="rubric").text.strip()
#             descriptions = new_list.find("span", class_="text").text.strip()
#             new_data_time = new_list.find("span", class_="date").text.strip()
#
#             news_dict[id_url] = {
#                 "data": new_data_time,
#                 "title": title,
#                 "descriptions": descriptions,
#                 "url": new_url
#             }
#
#             frefh_news[id_url] = {
#                 "data": new_data_time,
#                 "title": title,
#                 "descriptions": descriptions,
#                 "url": new_url
#             }
#     with open("news_dict.json", "w", encoding="UTF8") as file:
#         json.dump(news_dict, file, indent=4, ensure_ascii=False)
#
#     return frefh_news
#
# def main():
#     #     get_first_news()
#     check_news_update()
#
#
# if __name__ == "__main__":
#     main()
# get_first_news()