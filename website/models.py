from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import DateTime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'  

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    # Override get_id to take user_id instead of id 
    def get_id(self):
        return str(self.user_id)  

    def __repr__(self):
        return f'<User {self.username}>'
