from app import app, db, login_manager
from app.models import User, Row
from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user
import bcrypt


# static status
TODO = 'todo'
DOING = 'doing'
DONE = 'done'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
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
                return redirect(url_for('home'))
        # error
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    user.session.add(user)
    user.session.commit()
    logout_user()
    # flash('Logout realizado com sucesso!')
    return redirect(url_for('login'))


@app.route('/')
@app.route('/home')
@login_required
def home():
    user = current_user
    todo = Row.query.filter_by(user_id=user.id, status=TODO).all()
    doing = Row.query.filter_by(user_id=user.id, status=DOING).all()
    done = Row.query.filter_by(user_id=user.id, status=DONE).all()
    return render_template('home.html', user=user, todo=todo, doing=doing, done=done)


@app.route('/line/add/<status>', methods=['GET', 'POST'])
def add_line(status):
    user = current_user
    if request.method == 'POST':
        text = request.form['text']
        line = Row(text=text, status=status, user_id=user.id)
        db.session.add(line)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_line.html', user=user, status=status)