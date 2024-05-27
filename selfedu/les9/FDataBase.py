import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):  # db ссылка на связь с БД
        self.__db = db  # сохраняем ссылку в экземпляре этого класса
        self.__cur = db.cursor()  # через класс курсор работаем с таблицами в БД

    def getMenu(self):  # через метод происходит выборка всех запесей из таблицы меню
        sql = '''SELECT * FROM mainmenu'''
        try:  # работет через try на случай ошибок
            self.__cur.execute(sql)
            res = self.__cur.fetchall()  # вычитываем все записи
            if res: return res  # возозвращем их, если записи были прочитаны успешно
        except:
            print('Ошибка из БД')
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())  # округление до секунд в меньшую сторону
            self.__cur.execute("INSERT INTO posts VALUES (NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в БД ' + str(e))
            return False
        return True

    def getPost(self, postId):  # по postId выбирает нужную статью из таблицы posts
        try:
            # q = f"SELECT title, text FROM posts WHERE id = {postId}"
            # self.__cur.execute(q)
            self.__cur.execute(f'SELECT title, text FROM posts WHERE id = {postId} LIMIT 1')
            res = self.__cur.fetchone()  # fetchone - одна запись
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из БД ' + str(e))
        return (False, False)

    def getPostsAnonce(self):  # Все статьи для главной страницы
        try:
            self.__cur.execute(f'SELECT id, title, text FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))
        return []


