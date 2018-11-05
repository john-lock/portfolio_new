from flask import Flask
import unittest
from app import app, db, create_app
from app.models import User, Projects
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class UserModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        db = SQLAlchemy()
        db.init_app(app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password(self):
        u = User(username="jason")
        u.set_password("bigpass")
        self.assertFalse(u.check_password("small"))
        self.assertTues(u.check_password("bigpass"))


if __name__ == "__main__":
    unittest.main(verbosity=2)


# Test project creation

# User creation
# User func
# user pw

# contact

# Test Front end
