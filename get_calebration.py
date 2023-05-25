from bs4 import BeautifulSoup
import requests
import datetime

URL = 'https://my-calend.ru/holidays'
date = ''
YEAR_URL = 'https://my-calend.ru/holidays/2023'

month = {'января': '01', 'февраля': '02', 'марта': '03', 'апреля': '04', 'мая': '05', 'июня': '06', 'июля': '07',
         'августа': '08', 'сентября': '09', 'октября': '10', 'ноября': '11', 'декабря': '12', }

def get_day_html():
    global date
    with open('index_day.html', 'w', encoding='UTF-8') as file:
        file.write(requests.get(URL).text)
    date = datetime.date.today()

def get_year_html():
    with open('index_year.html', 'w', encoding='UTF-8') as file:
        file.write(requests.get(YEAR_URL).text)

def get_celebration():
    global date
    if datetime.date.today() != date:
        get_day_html()
    with open('index.html', 'r', encoding='UTF-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    celebrations = [
        item.text + '\n'
        for item in soup.select('ul.holidays-items span, ul.holidays-items a')
        if item.text.strip() and not item.text.strip().isdigit()
    ]

    return celebrations

def get_CelDay(input_date):
    with open('index_year.html', 'r', encoding="UTF-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    cur = soup.select('table.holidays-month-items a, table.holidays-month-items span:not(.grey, .holidays-weekday)')

    celebration = []

    triger = False

    for i in cur:
        i = i.text

        if triger and i[0].strip().isdigit():
            break

        if triger and i != '\xa0':
            celebration.append(i)

        if i != ' ' and i[1] == ' ':
            i = "0" + i

        if i[2:] in month or i[3:] in month:
            if input_date[:2] == i[:2] and month[i[3:]] == input_date[3:]:
                triger = True

    return celebration if celebration != [] else None
print(get_CelDay('31.13'))