from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('/data/database.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            tid INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS done (
            did INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            task_id INTEGER
        )
    """)

    conn.commit()
    conn.close()

init_db()

conn = sqlite3.connect('/data/database.db', check_same_thread=False)
cursor = conn.cursor()


@app.route('/addTask', methods=['GET'])
def add_task():
    task = request.args.get('task')
    cursor.execute("INSERT INTO tasks(task) VALUES(?)", (task,))
    conn.commit()
    return redirect('/')


@app.route('/getTasks', methods=['GET'])
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    row = cursor.fetchone()
    return render_template("index.html", tasks=row)

@app.route('/move-to-done/<int:id>/<string:task_name>')
def move_to_done(id, task_name):
    cursor.execute("INSERT INTO done(task, task_id) VALUES(?,?)", (task_name,id))
    cursor.execute("DELETE FROM tasks WHERE tid = ?", (id,))
    conn.commit()
    return redirect('/')

@app.route('/deleteTask/<int:id>')
def deleteTask(id):
    cursor.execute("DELETE FROM tasks WHERE tid=?", (id,))
    conn.commit()
    return redirect('/')


@app.route('/delete-completed/<int:id>')
def deleteCompletedTask(id):
    cursor.execute("DELETE FROM done WHERE did=?", (id,))
    conn.commit()
    return redirect('/')


@app.route('/')
def home():
    conn = sqlite3.connect('/data/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    row = cursor.fetchall() 
    cursor.execute("SELECT * FROM done")
    row2 = cursor.fetchall()
    return render_template('index.html', tasks=row, done=row2)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

