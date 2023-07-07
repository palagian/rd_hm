from flask import abort, redirect, request, render_template, session, url_for
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
     'title': 'Eneida'},
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

# 1. Створити html темплейти для кожного із ендпоінтів, що були створені під час виконання минулого ДЗ. Мають відображатися ті самі дані, але інтегровані
# в темплейти за допомогою контексту.
# - /users
# - /users/{id}
# - /books
# - /books/{id}
# - /params
# - /login
# - /

# 3. На всі сторінки додати перевірку на те, чи містить сесія імʼя користувача:
# - Якщо містить – відображати на самому початку сторінки текст "Hello, username", де username – імʼя користувача із сесії.
# - Якщо не містить – перенаправляти користувача на сторінку /login

@app.get ('/users')
def get_random_users():
    app.logger.info('get_random_users is called')
    username = session.get('username')
    count = request.args.get('count')
    if count is None:
        count = random.randint(1, len(names))
    elif int(count) > len(names):       # if requested number is higher than lenght of the list
        abort(400, 'We do not have so many users.')
    else:
        count = min(int(count), len(names))
    random_names = random.sample(names, k=count)
    return render_template('users/users.html', names=random_names, username=username)

@app.get ('/books')
def get_random_books():
    app.logger.info('get_random_books is called')
    username = session.get('username')
    count = request.args.get('count')
    if count is None:
        count = random.randint(1, len(books))
    elif int(count) > len(books):       # if requested number is higher than lenght of the list
        abort(400, 'We do not have so many books.')
    else:
        count = min(int(count), len(books))
    random_books = random.sample(books, k=count)
    return render_template('books/books.html', books=random_books, username=username)


@app.get ('/users/<int:user_id>')
def get_user(user_id):
    app.logger.info(f'get_user is called with user_id: {user_id}')
    username = session.get('username')
    # я додала додаткову умову до завдання: щоб шукав парні id саме в списку names. Тобто 404 помилка вийде для непарних id в names та для всіх id поза списком names.
    user = next((item for item in names if item['id'] == user_id and item['id'] % 2 == 0), None)
    if user:
        return render_template('users/users_id.html', user=user, username=username)
    else:
        abort(404, 'User not found')

@app.get ('/books/<string:title>')
def get_book(title):
    app.logger.info(f'get_book is called with title: {title}')
    username = session.get('username')
    transformed_title = title.capitalize()
    book = next((b for b in books if b['title'] == transformed_title), None)
    return render_template('books/books_id.html', title=transformed_title, book=book, username=username)


@app.get('/params')
def get_params():
    app.logger.info('get_params is called')
    username = session.get('username')
    parameters = request.args
    return render_template('params/params.html', parameters=parameters, username=username)


@app.get ('/login')
def login_get():
    app.logger.info('login_get is called')
    return render_template('login/login.html')

# 2. В ендпоінт /login, при заповненні форми, додати функціонал запису імені користувача в сесію.

app.secret_key = 'secret_key'
@app.post ('/login')
def login_post():
    app.logger.info('login_post is called')
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        username_pattern = r'^.{5,}$'
        password_pattern = r'^(?=.*\d)(?=.*[A-Z]).{8,}$'

        if re.match(username_pattern, username) and re.match(password_pattern, password):
            session['username'] = username
            return redirect(url_for('home', username=username))
        else:
            abort(400, 'Invalid username or password')
    else:
        abort(400, 'Missing username or password')

@app.errorhandler(404)
def page_not_found(error):
    return 'Opps, page not found', 404

@app.errorhandler(500)
def internal_server_error(error):
    return 'Oops, internal server error', 500


@app.get('/')
def home():
    app.logger.error('home is called')
    username = session.get('username')
    return render_template('home/home.html', username=username)

# 4. (необов'язкове виконання) На кожну сторінку додати кнопку logout, при натисканні якої користувач має видалятися із сесії і
# перенаправлятися на сторінку /login. Для цього потрібно реалізувати також окремий ендпоінт /logout.

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    app.logger.info('logout is called')
    session.pop('username', None)
    return redirect(url_for('login_get'))