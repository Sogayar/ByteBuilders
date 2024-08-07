from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class User(db.Model):
    id_u = db.Column(db.Integer, primary_key=True)
    name_u = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

class Worker(db.Model):
    id_w = db.Column(db.Integer, primary_key=True)
    worker = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)