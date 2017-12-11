import os
basedir = os.path.abspath(os.path.dirname(__file__))

dbdir = basedir + '/app/kanban.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + dbdir
SECRET_KEY = 'hellooooooooo'
