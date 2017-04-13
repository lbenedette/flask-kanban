from app import app, db, login_manager
from app.models import User, Task
from flask import render_template, request, redirect, url_for, flash
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
        email = request.form['email']
        name = request.form['name']
        last_name = request.form['last_name']
        password = request.form['password']
        re_password = request.form['re_password']
        user = User.query.filter_by(email=email).first()
        if user is None:
            if password == re_password:
                user = User(email=email, name=name, last_name=last_name, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
                db.session.add(user)
                db.session.commit()
                flash('Cadastrado com sucesso!', 'success')
                return redirect(url_for('login'))
            else:
                flash('A senha e a confirmação de senha devem ser iguais!', 'danger')
        else:
            flash('Endereço de email já cadastrado!', 'danger')
    return render_template('register.html', title='registrar')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.hashpw(password.encode(), user.password.encode()).decode() == user.password:
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('home'))
        flash('Email e/ou senha inválidos!', 'danger')
    return render_template('login.html', title='entrar')


@app.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    # flash('Logout realizado com sucesso!')
    return redirect(url_for('login'))


@app.route('/')
@app.route('/home')
@login_required
def home():
    user = current_user
    todo = Task.query.filter_by(user_id=user.id, status=TODO).all()
    doing = Task.query.filter_by(user_id=user.id, status=DOING).all()
    done = Task.query.filter_by(user_id=user.id, status=DONE).all()
    return render_template('home.html', title='home', user=user, todo=todo, doing=doing, done=done)


@app.route('/task/new/<status>', methods=['GET', 'POST'])
@login_required
def task_new(status):
    user = current_user
    if request.method == 'POST':
        text = request.form['text']
        if text:
            task = Task(text=text, status=status, user_id=user.id)
            db.session.add(task)
            db.session.commit()
            flash('Tarefa adicionada com sucesso', 'success')
            return redirect(url_for('home'))
        else:
            flash('Não é possível adicionar uma tarefa vazia!', 'warning')
    return render_template('task_new.html', title='nova tarefa', user=user, status=status)


@app.route('/task/delete/<int:task_id>')
@login_required
def task_delete(task_id):
    task = Task.query.get(task_id)
    if task is not None:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('home'))


@app.route('/task/update/<int:task_id>/<status>')
@login_required
def task_update_status(task_id, status):
    task = Task.query.get(task_id)
    if task is not None:
        task.status = status
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('home'))
