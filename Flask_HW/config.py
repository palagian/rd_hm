import os

class AppConfig:
    DEBUG = os.getenv('DEBUG')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://myuser:mypassword@db/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
