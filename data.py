# data.py
import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)')
    conn.commit()

def add_task(task):
    cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
