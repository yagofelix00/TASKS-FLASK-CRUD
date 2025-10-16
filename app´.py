from flask import Flask, request
from models import Task

app = Flask(__name__)

# CRUD
# Create, Read, Uodate and Delete
# Tabela: Tarefa

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return 'Test'

if __name__ == "__main)__":
    app.run(debug=True)