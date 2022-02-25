import telebot
import requests
from pyquery import PyQuery as pq

bot = telebot.TeleBot('5165817687:AAE-se9jb-6fJ3iGQDYI_dGRj7ZXO1BYjq0')


def get_quote():
    resp = requests.get('http://bashorg.org/random')
    page = pq(resp.content)
    text = page('.quote:first').text()
    id = page('.vote:first').text()
    return id + "\r\n\r\n" + text


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    q = get_quote()
    bot.send_message(message.from_user.id, q)


bot.polling(none_stop=True, interval=0)
