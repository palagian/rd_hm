# 3. Написати запит, який виведе всіх users і назви  всіх книжок, які вони купували, відсортувати дані за user_id.
# Результат має бути представлений у форматі: users.id, users.first_name, users.last_name, books.title
#
# ----------------------------------------------------------------------------------------------------------
#
# SQL запит:
#
# SELECT
#     users.id AS 'users.id',
#     users.first_name AS 'users.first_name',
#     users.last_name AS 'users.last_name',
#     books.title AS 'books.title'
# FROM users
# LEFT JOIN purchase ON users.id = purchase.user_id
# LEFT JOIN books ON purchase.book_id = books.id
# ORDER BY users.id;