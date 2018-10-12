from app import app
import sqlite3
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
from flask import Flask
from flask_login import LoginManager, UserMixin
from app import Config
from app.models import Projects

db = SQLAlchemy(app)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

Projects.__table__.drop(engine)
db.session.commit()
print("DB Reset")