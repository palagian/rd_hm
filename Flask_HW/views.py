from flask import abort, redirect, request, render_template, session, url_for, jsonify
import re
from app import db, app
from models import User, Book, Purchase

# 5. Модифікувати існуючі, або додати нові енпоінти. Дані відображати у форматі JSON або використовуючи HTML template:
# - GET /users — відобразити список всіх обʼєктів User (всі записи відповідної таблиці)
# - GET /users/<int:user_id> —- відобразити інформацію про User із відповідним id, або ж 404
# - GET /books —- відобразити список всіх обʼєктів Book (всі записи відповідної таблиці)
# - GET /books/<int:book_id> —- відобразити інформацію про Book із відповідним id, або ж 404
# - GET /purchases —- відобразити список всіх обʼєктів Purchase (всі записи відповідної таблиці)
# - GET /purchases/<int:purchase_id> —- відобразити інформацію про Purchase із відповідним id, або ж 404

# 6. (необов'язкове виконання) При передачі із запитом query param size=n для ендпоінтів зі списком обʼєктів, показувати
# відповідну кількість обʼєктів

@app.get ('/users')
def get_users():
    username = session.get('username')
    size = request.args.get('size')
    query = db.select(User)
    if size is not None:
        query = query.limit(size)
    users = db.session.execute(query).scalars()
    return render_template('users/users.html', users=users, username=username)

@app.get ('/books')
def get_random_books():
    username = session.get('username')
    size = request.args.get('size')
    query = db.select(Book)
    if size is not None:
        query = query.limit(size)
    books = db.session.execute(query).scalars()
    return render_template('books/books.html', books=books, username=username)


@app.get ('/users/<int:user_id>')
def get_user(user_id):
    username = session.get('username')
    user = User.query.get(user_id)
    if user:
        return render_template('users/users_id.html', user=user, username=username)
    else:
        abort(404, 'User not found')

@app.get ('/books/<int:book_id>')
def get_book(book_id):
    username = session.get('username')
    book = Book.query.get(book_id)
    if book:
        return render_template('books/books_id.html', book=book, username=username)
    else:
        abort(404, 'Book not found')

# 7. (необов'язкове виконання) При запиті на endpoint /purchases та /purchases/<int:purchase_id> виводити не лише інформацію
# про покупки, але і назву книжки та імʼя користувача, що її купив
@app.get('/purchases')
def get_purchases():
    username = session.get('username')
    size = request.args.get('size')
    query = db.select(Purchase)
    if size is not None:
        query = query.limit(size)
    purchases = db.session.execute(query).scalars()
    return render_template('purchases/purchases.html', purchases=purchases, username=username)

@app.get('/purchases/<int:purchase_id>')
def get_purchase(purchase_id):
    username = session.get('username')
    purchase = Purchase.query.get(purchase_id)
    if purchase:
        return render_template('purchases/purchases_id.html', purchase=purchase, username=username)
    else:
        abort(404, 'Purchase not found')


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


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    app.logger.info('logout is called')
    session.pop('username', None)
    return redirect(url_for('login_get'))

# 8. (необов'язкове виконання) Реалізувати можливість створення нових обʼєктів в базі даних. Ендпоінти можуть приймати
# "application/json" або "application/x-www-form-urlencoded":
# - POST /users
# - POST /books
# - POST /purchases (перевірити чи існують відповідні User та Book)

def validate_content_type():
    if request.content_type not in ['application/json', 'application/x-www-form-urlencoded']:
        return jsonify(message='Invalid content type'), 415
@app.post('/users')
def create_user():
    validate_content_type()

    name = request.form.get('name') or request.json.get('name')
    if name:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return jsonify(message='User created successfully'), 201
    else:
        return jsonify(message='Missing name parameter'), 400


@app.post('/books')
def create_book():
    validate_content_type()

    title = request.form.get('title') or request.json.get('title')
    if title:
        book = Book(title=title)
        db.session.add(book)
        db.session.commit()
        return jsonify(message='Book created successfully'), 201
    else:
        return jsonify(message='Missing title parameter'), 400


@app.post('/purchases')
def create_purchase():
    validate_content_type()

    user_id = request.form.get('user_id') or request.json.get('user_id')
    book_id = request.form.get('book_id') or request.json.get('book_id')

    if user_id and book_id:
        user = User.query.get(user_id)
        book = Book.query.get(book_id)

        if user and book:
            quantity = request.form.get('quantity') or request.json.get('quantity')
            if not quantity:
                quantity = 1

            purchase = Purchase(user=user, book=book, quantity=quantity)
            db.session.add(purchase)
            db.session.commit()
            return jsonify(message='Purchase created successfully'), 201
        else:
            return jsonify(message='User or book not found'), 404
    else:
        return jsonify(message='Missing user_id or book_id parameter'), 400
