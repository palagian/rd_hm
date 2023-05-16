# 1. Створити базу даних SQLite. Використовуючи SQL запити, в створеній базі даних створити таблицю, яка має
# містити наступні поля:
# id - значення для кожного нового елементу має за замовчуванням бути +1 від попереднього
# first_name — текстове значення
# last_name — текстове значення
# age — число

import sqlite3

connection = sqlite3.connect("my_db.db")

# sql request for task1:
#
# CREATE TABLE users
# (id INTEGER PRIMARY KEY AUTOINCREMENT ,
# first_name TEXT,
# last_name TEXT,
# age INTEGER);