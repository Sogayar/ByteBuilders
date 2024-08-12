import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/meus_dados' # username, password, localhost e meus_dados são os valores no banco de dados MySQL.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
