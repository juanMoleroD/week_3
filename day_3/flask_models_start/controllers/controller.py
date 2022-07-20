from app import app
from flask import render_template
from models.todo_list import tasks as all_tasks


@app.route('/')
def index():
    return "Hello World!"

@app.route('/tasks')
def tasks():
    return render_template('index.html', title="All Tasks" , all_tasks=all_tasks)

