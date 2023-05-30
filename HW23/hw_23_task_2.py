# 2. Написати запит, який виведе дату покупки і імʼя користувача, що її здійснив.
# Результат має бути представлений у форматі: purchases.id, purchases.date, user.first_name, user.last_name
#
# ----------------------------------------------------------------------------------------------------------
#
# SQL запит:
#
# SELECT
#     purchase.id AS 'purchase.id',
#     purchase.date AS 'purchase.date',
#     users.first_name AS 'users.first_name',
#     users.last_name AS 'users.last_name'
# FROM purchase
# LEFT JOIN users ON purchase.user_id = users.id;
