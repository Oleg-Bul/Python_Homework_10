import telebot
import cnfg
import model

bot = telebot.TeleBot(cnfg.TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f'Введите трехбуквенный код валюты\
    (USD, EUR, JPY, CNY и тд)')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f' Курс {model.get_name(message.text)} =\
 {model.get_value(message.text)} руб.')

print('server run')
bot.infinity_polling()
