from flask import abort, redirect, request
from app import app
import random
import re

names = [
    {'id': 1,
     'name': 'Alice'},
    {'id': 2,
     'name': 'Andrew'},
    {'id': 3,
     'name': 'Christina'},
    {'id': 4,
     'name': 'Danylo'},
    {'id': 5,
     'name': 'Taras'},
    {'id': 6,
     'name': 'Anhelina'},
    {'id': 7,
     'name': 'Julia'},
    {'id': 8,
     'name': 'Serhii'},
    {'id': 9,
     'name': 'Oleksandr'},
    {'id': 10,
     'name': 'Olha'},
]

books = [
    {'id': 1,
     'title': 'Kobzar'},
    {'id': 2,
     'titlee': 'Eneida'},
    {'id': 3,
     'title': '1984'},
    {'id': 4,
     'title': 'Lisova pisnia'},
    {'id': 5,
     'title': 'Harry Potter'},
    {'id': 6,
     'title': 'Romeo and Juliet'},
    {'id': 7,
     'title': 'Alchemist'},
    {'id': 8,
     'title': 'Instytutka'},
    {'id': 9,
     'title': 'Tini zabutykh predkiv'},
    {'id': 10,
     'title': 'Kaidasheva simya'},
]

# 1. Створити функції для обробки таких запитів:
# - GET /users – має повертати рандомний список імен (будь-яку кількість)
# - GET /books – має повертати рандомний список книжок (будь-яку кількість) у вигляді html списку

# 7. (необов'язкове виконання) Модифікувати функції обробники /users та /books із першого завдання таким чином, щоб вони повертали точну
# кількість значень на основі query param count: /users?count=20 має повернути 20 значень. Якщо параметр не передано — кількість має бути рандомною.

@app.get ('/users')
def get_random_users():
    app.logger.info('get_random_users is called')
    count = request.args.get('count')
    if count is None:
        count = random.randint(1, len(names))
    elif int(count) > len(names):       # if requested number is higher than lenght of the list
        abort(400, 'We do not have so many users.')
    else:
        count = min(int(count), len(names))
    random_names = random.sample(names, k=count)
    return random_names

@app.get ('/books')
def get_random_books():
    app.logger.info('get_random_books is called')
    count = request.args.get('count')
    if count is None:
        count = random.randint(1, len(books))
    elif int(count) > len(books):       # if requested number is higher than lenght of the list
        abort(400, 'We do not have so many books.')
    else:
        count = min(int(count), len(books))
    random_books = random.sample(books, k=count)

    response = "<h1>Books list:</h1>\n<ul>\n"

    for book in random_books:
        response += f"<li>{book['title']}</li>\n"
    response += "</ul>"

    return response

# 2. Створити функції-обробники запитів на GET  /users та GET /books, що мають приймати url-параметри (/users/1, /books/kobzar):
# - Для /users – id, що може бути тільки числовим значенням. Якщо значення id ділиться на 2 - повертати текст із цим значенням.
# Якщо не ділиться – повертати статус 404 Not Found
# - Для /books – title, текстове значення. Трансформувати першу літеру title у велику, а всі інші у маленькі (за допомогою одного
# із методів str), повернути трансформоване значення у якості відповіді

@app.get ('/users/<int:user_id>')
def get_user(user_id):
    app.logger.info(f'get_user is called with user_id: {user_id}')
    # я додала додаткову умову до завдання: щоб шукав парні id саме в списку names. Тобто 404 помилка вийде для непарних id в names та для всіх id поза списком names.
    user = next((item for item in names if item['id'] == user_id and item['id'] % 2 == 0), None)
    if user:
        return f"User id: {user_id}, Name: {user['name']}"
    else:
        abort(404, 'User not found')

@app.get ('/books/<string:title>')
def get_book(title):
    app.logger.info(f'get_book is called with title: {title}')
    transformed_title = title.capitalize()
    return transformed_title

# 3. Створити функцію для обробки запитів GET /params – має повертати HTML таблицю, в якій будуть міститися ключі та значення query parameters.
# Наприклад, при запиті GET /params?name=Test&age=1, на сторінці має відобразитися:
# parameter | value
# name      | Test
# age       | 1

@app.get('/params')
def get_params():
    app.logger.info('get_params is called')
    parameters = request.args
    response = "<h1>Query Parameters:</h1>\n<table>\n<tr><th>Parameter</th><th>Value</th></tr>\n"

    for key, value in parameters.items():
        response += f"<tr><td>{key}</td><td>{value}</td></tr>\n"

    response += "</table>"
    return response

# 4. Створити функцію для обробки запитів GET, POST /login – при запиті GET має повертати HTML форму (method=POST, action=/login),
# що має містити поля username, password та кнопку submit.
# При запиті POST має перевіряти чи містяться в даних запиту username та password:
# - Якщо запит містить ці дані, потрібно перенаправити користувача на сторінку /users.
# - Якщо ні – потрібно повернути помилку 400 із інформацією про відсутні дані.

# 8. (необов'язкове виконання) До функції обробника POST /login додати валідацію username та password:
# - Username не менше 5 символів
# - Password має містити мінімум 1 цифру і 1 велику літеру, має бути не менше ніж 8 символів

@app.get ('/login')
def login_get():
    app.logger.info('login_get is called')
    return """
            <h1>Login Form</h1>
                <form method="POST" action="/login">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username"><br><br>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password"><br><br>
                    <input type="submit" value="Submit">
                </form>
            """

@app.post ('/login')
def login_post():
    app.logger.info('login_post is called')
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        username_pattern = r'^.{5,}$'
        password_pattern = r'^(?=.*\d)(?=.*[A-Z]).{8,}$'

        if re.match(username_pattern, username) and re.match(password_pattern, password):
            return redirect('/users')
        else:
            abort(400, 'Invalid username or password')
    else:
        abort(400, 'Missing username or password')

# 5. (необов'язкове виконання) Створити кастомні обробники помилок 404 та 500, що мають повертати кастомних html код для відображення.

@app.errorhandler(404)
def page_not_found(error):
    return 'Opps, page not found', 404

@app.errorhandler(500)
def internal_server_error(error):
    return 'Oops, internal server error', 500

# 6. (необов'язкове виконання) Створити обробник запиту GET /, що має повертати html код із посиланнями на сторінки /login, /users, /books, /params

@app.get('/')
def home():
    app.logger.error('home is called')
    return '''
        <h1>Welcome to the Homepage!</h1>
        <ul>
            <li><a href="/login">Login</a></li>
            <li><a href="/users">Users</a></li>
            <li><a href="/books">Books</a></li>
            <li><a href="/params">Params</a></li>
        </ul>
    '''