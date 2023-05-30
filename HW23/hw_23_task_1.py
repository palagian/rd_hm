# 1. Для обліку інформації про користувачів, книжки, видавництва та продажі створити наступні таблиці:
# users: id, first_name, last_name, age
# publishing_house: id, name, rating (default 5)
# books: id, title, author, year, price, publishing_house_id
# purchases: id, user_id, book_id, date
#
# При цьому:
# publishing_house_id — це FOREIGN KEY таблиці publishing_houses
# user_id —  це FOREIGN KEY таблиці users
# book_id —  це FOREIGN KEY таблиці books
#
# ----------------------------------------------------------------------------------------------------------
#
# SQL запит:
#
# CREATE TABLE users
# (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER
# );
#
# CREATE TABLE publishing_houses
# (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     rating INTEGER DEFAULT 5
# );
#
# CREATE TABLE books
# (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     author TEXT,
#     year INTEGER,
#     price INTEGER,
#     publishing_house_id INTEGER NOT NULL,
#     FOREIGN KEY (publishing_house_id) REFERENCES publishing_houses (id)
# );
#
# CREATE TABLE purchases
# (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER NOT NULL,
#     book_id INTEGER NOT NULL,
#     date1 TEXT DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (user_id) REFERENCES users (id),
#     FOREIGN KEY (book_id) REFERENCES books (id)
# );