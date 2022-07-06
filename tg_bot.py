import os
import sqlite3
import telebot
from config import *
from db_classs import Scraping_db

bot = telebot.TeleBot(API_TOKEN)

class Tg_Bot:

    def __init__(self, db_scraping):
        self.db_scraping = db_scraping
        self.scraping_db = Scraping_db(db_scraping, bot)

    def start_db(self, message):
        '''
        при команде /start создает поле с его id и нулевыми значениями для всех полей
        :return:
        '''

        id_user = message.chat.id
        surname = ''
        name = ''
        patronymic = ''
        phone_number = 0
        amount_of_investment = 0
        date = 0
        self.scraping_db.connect()
        self.scraping_db.create_db()
        cur = self.scraping_db.sqlite.cursor()
        print('id_user', id_user)
        user_id = self.scraping_db.find_id(id_user)
        print('user_id', user_id)
        if user_id == 1:
            pass
        else:
            self.scraping_db.create_post(id_user, surname, name, patronymic, phone_number, amount_of_investment, date)

        self.scraping_db.commit_db()
        cur.close()

    def update_surname_o(self, surname, id_user):
        ''' update surname user db '''
        self.scraping_db.connect()
        self.scraping_db.update_surname(surname, id_user)

    def update_name_o(self, name, id_user):
        ''' update name user db '''
        self.scraping_db.connect()
        self.scraping_db.update_name(name, id_user)

    def update_patronymic_o(self, patronymic, id_user):
        ''' update patronymic user db '''
        self.scraping_db.connect()
        self.scraping_db.update_patronymic(patronymic, id_user)

    def update_phone_number_o(self, phone_number, id_user):
        ''' update patronymic user db '''
        self.scraping_db.connect()
        self.scraping_db.update_phone_number(phone_number, id_user)

    def update_amount_of_investment_o(self, amount_of_investment, id_user):
        ''' update amount of investment user db '''
        self.scraping_db.connect()
        self.scraping_db.update_amount_of_investment(amount_of_investment, id_user)

    def update_date_o(self, date, id_user):
        ''' update date amount of investment user db '''
        self.scraping_db.connect()
        self.scraping_db.update_date(date, id_user)

    def update_amount(self, message):
        '''
        принимает значение X и id, что увеличить инвестиции
        :param message:
        :return:
        '''
        self.scraping_db.connect()
        message_text = message.text.split(' ')
        print(message_text)
        id_user = message_text[2]
        amount = self.scraping_db.subscription_expiration(id_user)
        print('amount[0] = ', amount[0], type(amount[0]), 'message_text[1]: ', message_text[1], type(message_text[1]), type(int(message_text[1])))
        amount_sum = amount[0] + int(message_text[1])
        print('amount_sum: ', amount_sum, 'id_use: ', id_user)
        self.scraping_db.update_amount_of_investment(amount_sum, id_user)
        bot.send_message(id_user, f'Ваши инвестиции увеличены на {amount_sum} \n введите команду /amount что бы узнать'
                                  f'сумму ваших инвестиций')
        self.scraping_db.update_date(message.date, id_user)

    def amount_return(self, message):
        self.scraping_db.connect()
        sum = self.scraping_db.subscription_expiration(message.chat.id)
        bot.send_message(message.chat.id, sum)

