from app import app, db, login_manager
from models import User
from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user
import bcrypt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(request.form)
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User(username=username, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        # username já cadastrado
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            if bcrypt.hashpw(password.encode(), user.password.encode()).decode() == user.password:
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('hello_world'))
        # error
    return render_template('login.html')


@app.route('/')
@login_required
def hello_world():
    return 'Hello World!'


@app.route('/<name>')
def name(name):
    return 'Hello ' + name
