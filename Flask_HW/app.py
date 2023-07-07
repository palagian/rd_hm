from flask import Flask
from logging.config import dictConfig

#4. Налаштувати логування у будь-якому форматі. Додати INFO логи у всі три функції.
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

# 2. Встановити Flask та створити flask application із ендпоінтом hello (GET). Ендпоінт має повертати текст "Hello, world!". (http://localhost:5000/hello)

@app.route('/hello')
def hello_world():
    app.logger.info('hello_world is called')
    return 'Hello, world!'

# 3. Додати ще два ендпоінта: один щоб повертав html, інший - json

@app.route('/html')
def products():
    app.logger.info('products is called')
    return 'milk, coffee, bread, butter'
#
@app.route('/json')
def users():
    app.logger.info('users is called')
    return [
        {
            'name': 'Anastasiia',
            'surname': 'Palahina',
            'age': 36
        },
        {
            'name': 'Oleksii',
            'surname': 'Kovalenko',
            'age': 37
        }
    ]


from views import *

if __name__ == '__main__':
    app.run(debug=True)
