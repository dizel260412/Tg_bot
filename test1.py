from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


def scr():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    serv = Service(r'C:\Users\Дом\Desktop\TG_BOT\chromedriver.exe')
    driver = webdriver.Chrome(service=serv
                              , options=options)
    driver.get('https://www.livesport.com/ru/football/')
    prev_html = driver.page_source
    with open('summary.html', 'w', encoding="UTF-8") as f:
        f.write(prev_html)
    driver.quit()


def cards():
    with open('summary.html', 'r', encoding="UTF-8") as f:
        sum_html = f.read()
        soup = BeautifulSoup(sum_html, "lxml")
        events_live = soup.find_all("div", title="Подробности матча!")
        # print(events_live)
        for ev in events_live:
            url = f'https://www.livesport.com/ru/match/{ev.get("id")[4:]}'
            t_title = ev.find_previous().find_previous().find_previous().find_previous().find_previous().find_previous() \
                .find_previous().text
            t_name = ev.find_previous().find_previous().find_previous().find_previous().find_previous().find_previous().text

            try:
                away = ev.find("div", class_="event__participant event__participant--away").text
                score_home = ev.find("div", class_="event__score event__score--home").text
                score_away = ev.find("div", class_="event__score event__score--away").text
                try:
                    home = ev.find("div", class_="event__participant event__participant--home").text
                    time = ev.find("div", class_="event__time").text
                except:
                    home = ev.find("div", class_="event__participant event__participant--home fontBold").text
                    time = ev.find("div", class_="event__stage--block").text


            except Exception as ex:
                continue
            print(f'{t_title}, {t_name}\n|{time}| {home} |{score_home}:{score_away}| {away}\n{url}')

            # try:
            #
            #     home = ev.find("div", class_="event__participant event__participant--home").text
            #     away = ev.find("div", class_="event__participant eve++nt__participant--away").text
            #     score_home = ev.find("div", class_="event__score event__score--home").text
            #     score_away = ev.find("div", class_="event__score event__score--away").text
            #     try:
            #         time = ev.find("div", class_="event__stage--block").text
            #
            #     except Exception as ex:
            #         time = ev.find("div", class_="event__time").text
            # except Exception as ex:
            #     continue


def main():
    scr()
    #cards()


if __name__ == "__main__":
    main()
