# 4. (необов'язкове виконання) Написати наступні запити:
# 4.1 запит, який для кожного user порахує суму всіх покупок. Результат має бути представлений у форматі: users.id,
# users.first_name, users.last_name, total_purchases
# 4.2 запит, який виведе кількість покупок книжок для кожного user. Результат має бути представлений у форматі:
# user.id, purchases_count
# 4.3 запит, який виведе кількість покупок книжок для автора Rowling. Результат має бути представлений у форматі:
# amount
# 4.4 запит, який виведе загальні суми продажів для кожного автора та кількість покупок.
# 4.5 запит, який виведе всі назви книжок із кількістю їх продажів в порядку спадання кількості продажів.
#
# ----------------------------------------------------------------------------------------------------------
#
# SQL запит 4.1:
#
# SELECT
#     users.id AS 'users.id',
#     users.first_name AS 'users.first_name',
#     users.last_name AS 'users.last_name',
#     SUM(books.price) AS 'total_purchases'
# FROM users
# LEFT JOIN purchase ON users.id = purchase.user_id
# LEFT JOIN books ON purchase.book_id = books.id
# GROUP BY users.id, users.first_name, users.last_name;
#
# -----------------------------------------------------------------------------------------------------------
#
# SQL запит 4.2:
#
# SELECT
#     users.id AS 'users.id',
#     COUNT(purchase.id) AS 'purchases_count'
# FROM users
# LEFT JOIN purchase ON users.id = purchase.user_id
# GROUP BY users.id, users.first_name, users.last_name;
#
# -----------------------------------------------------------------------------------------------------------
#
# SQL запит 4.3:
#
# SELECT COUNT(*) AS 'amount'
# FROM books
# JOIN purchase ON books.id = purchase.book_id
# WHERE books.author = 'Rowling';
#
# -----------------------------------------------------------------------------------------------------------
#
# SQL запит 4.4:
#
# SELECT
#     books.author AS 'author',
#     SUM(purchase.book_id) AS 'total_purchases',
#     COUNT(purchase.book_id) AS 'count_purchases'
# FROM books
# LEFT JOIN purchase ON books.id = purchase.book_id
# GROUP BY books.author;
#
# -----------------------------------------------------------------------------------------------------------
#
# SQL запит 4.5 (додала і суму продажів і к-сть продажів, сортування по к-сті):
#
# SELECT
#     books.title AS 'Title',
#     SUM(purchase.book_id) AS 'total_purchases',
#     COUNT(purchase.book_id) AS 'count_purchases'
# FROM books
# LEFT JOIN purchase ON books.id = purchase.book_id
# GROUP BY books.title
# ORDER BY count_purchases DESC;