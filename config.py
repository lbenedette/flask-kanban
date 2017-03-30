import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2:///kanban'
SECRET_KEY = 'hellooooooooo'