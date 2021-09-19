import requests


def currency_rates(currency):
    result = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    for line in result.text.split("/Valute><Valute"):
        if currency in line:
            cur = line.find(currency)
            nominal1 = line.find("</Nom")
            nominal2 = line.find("l>")+2
            value1 = line.find("ue>")+3
            value2 = line.find("</Val")
            return f"{line[nominal2: nominal1]} {line[cur: cur + 3]} = {line[value1: value2]} руб."
