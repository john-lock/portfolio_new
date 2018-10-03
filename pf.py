from app import app
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolioprojects.db')
db = SQLAlchemy(app)

class Projects(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    show = db.Column(db.Boolean, default=True)
    card_text = db.Column(db.String(400))
    modal_body = db.Column(db.TEXT)
    modal_short = db.Column(db.TEXT)
    modal_tech = db.Column(db.String(400))
