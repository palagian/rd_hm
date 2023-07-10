import logging
from flask import Flask
from dotenv import load_dotenv
from config import AppConfig
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config.from_object(AppConfig)
db.init_app(app)

from views import *
from models import *

with app.app_context():
    db.create_all()

# 3. Замінити в коді всі секретні значення на значення із environment

if __name__ == '__main__':
    app.run(host=AppConfig.HOST,
            port=AppConfig.PORT,
            debug=AppConfig.DEBUG)
