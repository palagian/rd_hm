# 3. (необов'язкове виконання) Для запиту створення таблиці із завдання 1 змінити first_name та last_name таким чином,
# щоб неможливо було додати пусте значення.

# 4. (необов'язкове виконання) Для запиту створення таблиці із завдання 1 змінити first_name та last_name таким чином,
# щоб неможливо було додати вже існуючу комбінацію first_name та last_name.

# sql request for tasks 3 and 4:
#
# CREATE TABLE users
# (id INTEGER PRIMARY KEY AUTOINCREMENT ,
# first_name TEXT NOT NULL,
# last_name TEXT NOT NULL,
# age INTEGER,
# CONSTRAINT unique_name_combination UNIQUE (first_name, last_name));