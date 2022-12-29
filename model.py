import requests


def get_valute(code):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return data['Valute'][code]['Value']
