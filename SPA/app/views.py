from app import app, db
from app.models import Task
from flask import render_template, request, redirect, url_for, flash, jsonify


# static status
TODO = 'todo'
DOING = 'doing'
DONE = 'done'


@app.route('/')
def home():
    todo = Task.query.filter_by(status=TODO).all()
    doing = Task.query.filter_by(status=DOING).all()
    done = Task.query.filter_by(status=DONE).all()
    return render_template('home.html', title='home', todo=todo, doing=doing, done=done)


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    response = {
        'todo': [item.serialize for item in Task.query.filter_by(status=TODO).all()],
        'doing': [item.serialize for item in Task.query.filter_by(status=DOING).all()],
        'done': [item.serialize for item in Task.query.filter_by(status=DONE).all()],
    }
    return jsonify(response)


@app.route('/task/new/<status>', methods=['GET', 'POST'])
def task_new(status):
    if request.method == 'POST':
        text = request.form['text']
        if text:
            task = Task(text=text, status=status)
            db.session.add(task)
            db.session.commit()
            flash('Tarefa adicionada com sucesso', 'success')
            return redirect(url_for('home'))
        else:
            flash('Não é possível adicionar uma tarefa vazia!', 'warning')
    return render_template('task_new.html', title='nova tarefa', status=status)


@app.route('/task/delete/<int:task_id>')
def task_delete(task_id):
    task = Task.query.get(task_id)
    if task is not None:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('home'))


@app.route('/task/update/<int:task_id>/<status>')
def task_update_status(task_id, status):
    task = Task.query.get(task_id)
    if task is not None:
        task.status = status
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('home'))


@app.route('/api/task/update/<int:task_id>/<status>')
def update_task(task_id, status):
    task = Task.query.get(task_id)
    if task is not None:
        task.status = status
        db.session.add(task)
        db.session.commit()
        response = {
            'todo': [item.serialize for item in Task.query.filter_by(status=TODO).all()],
            'doing': [item.serialize for item in Task.query.filter_by(status=DOING).all()],
            'done': [item.serialize for item in Task.query.filter_by(status=DONE).all()],
        }
        return jsonify(response)
    return jsonify({})
