import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ('DATABASE_URL')
SECRET_KEY = 'hellooooooooo'