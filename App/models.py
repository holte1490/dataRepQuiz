from BCS.App.app import db
from passlib.hash import bcrypt


class Questions(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    category: str = db.Column(db.String, index=True)
    question: str = db.Column(db.String, index=True)
    answer: str = db.Column(db.String, index=True)

    def __repr__(self):
        return '<Questions %r>' % self.category


class Users(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String, index=True, unique=True)
    email: str = db.Column(db.String, index=True)
    password: str = db.Column(db.String, index=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.encrypt(password)

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return "<User(username ='%s', password='%s', email='%s')>" % (self.username, self.password, self.email)
