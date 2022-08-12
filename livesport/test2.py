import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / "
                  "99.0.4844.51 Safari / 537.36"
}

url = "https://www.championat.com/football/_russiapl/tournament/4465/calendar/"
r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
with open('test3.html', 'w', encoding="UTF-8") as file:
    file.write(r.text)
