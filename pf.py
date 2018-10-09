from app import app
import sqlite3
import psycopg2
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
from flask_login import LoginManager, UserMixin

db = SQLAlchemy(app)

db.init()
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
