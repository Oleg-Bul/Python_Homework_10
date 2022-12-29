import requests


def get_valute(code):
    if code.upper() == 'RUB':
        return 1
    else:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        return data['Valute'][code.upper()]['Value']
