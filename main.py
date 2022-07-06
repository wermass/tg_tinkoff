from tg_bot import Tg_Bot
from db_classs import Scraping_db
import telebot
from telebot import types
from config import *

scraping = Tg_Bot('sqlite_python.db')

bot = telebot.TeleBot(API_TOKEN)
print('start')

@bot.message_handler(commands=['start'])
def start(message):
    scraping.start_db(message)
    mesg = bot.send_message(message.chat.id, 'Здравствуйте, напишите свою фамилию')
    bot.register_next_step_handler(mesg, test)


def test(message):
    print('surname = ', message.text, 'id user = ', message.chat.id)
    scraping.update_surname_o(message.chat.id, message.text)
    mesg1 = bot.send_message(message.chat.id, 'Напишите пожалуйста своё имя')
    bot.register_next_step_handler(mesg1, test1)

def test1(message):
    print('name = ', message.text)
    scraping.update_name_o(message.text, message.chat.id)
    mesg2 = bot.send_message(message.chat.id, 'Напишите пожалуйста своё отчество')
    bot.register_next_step_handler(mesg2, test2)

def test2(message):
    print('patronymic = ', message.text)
    scraping.update_patronymic_o(message.text, message.chat.id)
    mesg3 = bot.send_message(message.chat.id, 'Напишите пожалуйста свой телефон')
    bot.register_next_step_handler(mesg3, test3)

def test3(message):
    print('phone nomber = ', message.text, type(message.text))
    scraping.update_phone_number_o(message.text, message.chat.id)
    bot.send_message(message.chat.id, 'перенаправляем Вас на оператора @wermass')
    bot.send_message(id_my, f'пользователь {message.from_user.username} c id {message.from_user.id} прошел регистрацию')

@bot.message_handler(commands=['update'])
def update(message):
    if message.chat.id == id_my:
        scraping.update_amount(message)

@bot.message_handler(commands=['amount'])
def to_know(message):
    scraping.amount_return(message)

@bot.message_handler(commands=['print'])
def to_know(message):
    print(message)

bot.infinity_polling()
