from bs4 import BeautifulSoup
import requests
import datetime

URL = 'https://my-calend.ru/holidays'
date = ''

def get_html():
    global date
    with open('index.html', 'w', encoding='UTF-8') as file:
        file.write(requests.get(URL).text)
    date = datetime.date.today()

def get_celebration():
    global date
    if datetime.date.today() != date:
        get_html()
    with open('index.html', 'r', encoding='UTF-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    celebrations = [
        item.text + '\n'
        for item in soup.select('ul.holidays-items span, ul.holidays-items a')
        if item.text.strip() and not item.text.strip().isdigit()
    ]

    return celebrations
