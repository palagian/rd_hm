# 3. Написати sql запит, який виведе інформацію про вік (кількість років) та кількість користувачів, які
# відповідають цьому віку. Результатом виконання такого запиту має бути таблиця:
#     age  | users
#     32    | 1
#     52    | 2
#     120  | 2
#     1142 | 1
#
#
#
# Якщо результатом має бути таблиця в завданні, то треба зробити додатковe фільтрування, щоб не виводились
# роки < 30 (цього в завданні не написано, але я орієнтуюсь на вихідну таблицю)
# SQL запит:
# SELECT age, COUNT (id) AS users FROM users WHERE age > 30 GROUP BY age;