from app import app
import sqlite3
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
from flask import Flask
from flask_login import LoginManager, UserMixin
from app import Config

db = SQLAlchemy(app)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

login_manager = LoginManager()
login_manager.init_app(app)
