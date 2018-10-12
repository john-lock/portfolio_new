import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'portfolioprojects.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SENDGRID_API_KEY = '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'
    ADMIN_PW = os.environ.get('ADMIN_PW')
