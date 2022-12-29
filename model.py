import requests


def get_value(code):
    if code.upper() == 'RUB':
        return 1
    else:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        return data['Valute'][code.upper()]['Value']


def get_name(code):
    if code.upper() == 'RUB':
        return 'Российский Рубль'
    else:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        return data['Valute'][code.upper()]['Name']
