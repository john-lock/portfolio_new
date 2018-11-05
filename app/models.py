from app import app
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, UserMixin
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

admin_user = os.environ["admin_user"]
admin_pw = os.environ["admin_pw"]


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Projects(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    idname = db.Column(db.String(200))
    card_text = db.Column(db.String(400))
    modal_body = db.Column(db.TEXT)
    modal_short = db.Column(db.TEXT)
    modal_tech = db.Column(db.String(400))
    preview = db.Column(db.String(200))
    github = db.Column(db.String(200))
    show = db.Column(db.String(20))
    top = db.Column(db.String(20))
    images = db.Column(db.Integer)


db.create_all()
db.session.commit()


# add admin user if there are no users
allusers = User.query.all()
if (len(allusers)) > 0:
    pass
else:
    admin = User(admin_user)
    admin.set_password(admin_pw)
    db.session.add(admin)
    db.session.commit()
