import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import requests


def src(url, f_name):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    serv = Service(r'C:\Users\datel3\OneDrive - IKEA\Desktop\Python\Tg_bot\chromedriver.exe')
    driver = webdriver.Chrome(service=serv
                              , options=options)
    driver.get(url=url)
    prev_html = driver.page_source
    with open(f_name, 'w', encoding="UTF-8") as f:
        f.write(prev_html)

    driver.quit()


def events(f_name):
    with open(f_name, 'r', encoding="UTF-8") as f:
        sum_html = f.read()
        soup = BeautifulSoup(sum_html, "lxml")
        events_live = soup.find_all("div", title="Подробности матча!")
        print((events_live))
        events_dict = {}
        for ev in events_live:
            t_title = ev.find_previous().find_previous().find_previous().find_previous().find_previous()\
                .find_previous().find_previous().text
            t_name = ev.find_previous().find_previous().find_previous().find_previous().find_previous()\
                .find_previous().text
            try:
                id_url = ev.get("id")[4:]
                url = f'https://www.livesport.com/ru/match/{id_url}'
                away = ev.find("div", class_="event__participant event__participant--away").text
                score_home = ev.find("div", class_="event__score event__score--home").text
                score_away = ev.find("div", class_="event__score event__score--away").text
                try:
                    home = ev.find("div", class_="event__participant event__participant--home").text
                except:
                    home = ev.find("div", class_="event__participant event__participant--home fontBold").text
                try:
                    time = ev.find("div", class_="event__time").text.replase('\xa0', '')
                except:
                    time = ev.find("div", class_="event__stage--block").text


            except Exception as ex:
                continue
            events_dict[url] = {
                "country": t_title,
                "ligue": t_name,
                "time": time,
                "home_name": home,
                "home_score": score_home,
                "away_score": score_away,
                "away_name": away,
                "url": url
            }

        with open("events_dict_APL.json", "w", encoding="UTF8") as file:
            json.dump(events_dict, file, indent=4, ensure_ascii=False)


def title():
    with open("events_dict_sport.json", "r", encoding="UTF-8") as file:
        all_categories = json.load(file)

        i = 1
        for url, value in all_categories.items():
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            serv = Service(r'C:\Users\datel3\OneDrive - IKEA\Desktop\Python\Tg_bot\chromedriver.exe')
            driver = webdriver.Chrome(service=serv
                                      , options=options)
            driver.get(url=url)
            time.sleep(2)
            prev_html = driver.page_source
            with open(f'{i}', 'w', encoding="UTF-8") as f:
                f.write(prev_html)
            i += 1
            driver.quit()
            time.sleep(2)


def main():
    url = 'https://www.livesport.com/ru/football/england/premier-league/'
    f_name = 'summary_APL.html'
    # src(url, f_name)
    events(f_name)
    # title()


if __name__ == "__main__":
    main()

