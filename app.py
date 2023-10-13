# app.py
from flask import Flask, request

app = Flask(__name)

@app.route("/add_task", methods=["POST"])
def add_task():
    # Get the task from the request
    task = request.form.get("task")
    # Add the task to the database
    # (We will implement this in the Data Tier)
    return "Task added successfully!"

if __name__ == "__main__":
    app.run(debug=True)
