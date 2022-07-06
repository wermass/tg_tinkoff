import os
import sqlite3
import time
import telebot
from config import *

class Scraping_db:

    def __init__(self, scraping_db, bot):
        self.scraping_db = scraping_db
        self.bot = bot

    def connect(self):
        '''
        создаем таблицу +
        :return:
        '''
        if not os.path.exists(self.scraping_db):
            print('Error not file')  # можно создать

        self.sqlite = sqlite3.connect(self.scraping_db)  # создаем таблицу с именем в скобках

    def create_db(self):
        '''
        создаем таблицу в базе при первом запуске ++
        :return:
        '''
        self.sqlite.execute("""CREATE TABLE IF NOT EXISTS scraping(    
                   id_user int,
                   surname TEXT,
                   name TEXT,
                   patronymic TEXT,
                   phone_number int,
                   amount_of_investment int,
                   date int
                                    
                   ); 
                """)
        self.sqlite.commit()

    def find_id(self, id_user):
        '''
        найти пользователя по по id_user +
        '''
        info = self.sqlite.cursor().execute("SELECT id_user FROM scraping WHERE id_user = ?", (id_user, ))
        if info.fetchone() is None:
            return 0
            # Делаем когда нету человека в бд
        else:
            return 1
             # Делаем когда есть человек в бд

    def commit_db(self):
        '''
        коментируем
        :return:
        '''
        self.sqlite.commit()

    def create_post(self, id_user, surname, name, patronymic, phone_number, amount_of_investment, date):
        '''
        insert new user db
        :param id_user:
        :param surname:
        :param name:
        :param patronymic:
        :param phone_number:
        :param amount_of_investment:
        :param date:
        :return:
        '''

        sqlite_insert_with_param = """INSERT INTO scraping
             (id_user, surname, name, patronymic, phone_number, amount_of_investment, date)
             VALUES (?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (id_user, surname, name, patronymic, phone_number, amount_of_investment, date)

        self.sqlite.cursor().execute(sqlite_insert_with_param, data_tuple)

    def update_surname(self, surname, id_user):
        ''' update surname user db '''
        self.sqlite.cursor().execute("UPDATE scraping SET surname = ? WHERE id_user = ?", (surname, id_user,))
        self.sqlite.commit()
        self.sqlite.close()

    def update_name(self, name, id_user):
        ''' update name user db '''
        self.sqlite.cursor().execute("UPDATE scraping SET name = ? WHERE id_user = ?", (name, id_user,))
        self.sqlite.commit()
        self.sqlite.close()

    def update_patronymic(self, patronymic, id_user):
        ''' update patronymic user db '''
        self.sqlite.cursor().execute("UPDATE scraping SET patronymic = ? WHERE id_user = ?", (patronymic, id_user,))
        self.sqlite.commit()
        self.sqlite.close()

    def update_phone_number(self, phone_number, id_user):
        ''' update patronymic user db '''
        self.sqlite.cursor().execute("UPDATE scraping SET phone_number = ? WHERE id_user = ?", (phone_number, id_user,))
        self.sqlite.commit()
        self.sqlite.close()

    def update_amount_of_investment(self, amount_of_investment, id_user):
        ''' update amount of investment user db '''
        self.sqlite.cursor().execute("UPDATE scraping SET amount_of_investment = ? WHERE id_user = ?", (amount_of_investment, id_user,))
        self.sqlite.commit()
        self.sqlite.close()

    def update_date(self, date, id_user):
        ''' update date amount of investment user db '''
        self.sqlite.cursor().execute("UPDATE scraping SET date = ? WHERE id_user = ?", (date, id_user,))
        self.sqlite.commit()
        self.sqlite.close()

    def subscription_expiration(self, id_user):
        ''' сколько уже инвестировал '''
        self.connect()
        return self.sqlite.cursor().execute("SELECT amount_of_investment FROM scraping WHERE id_user = ?", (id_user, )).fetchone()
