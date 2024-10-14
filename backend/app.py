from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir requisições CORS

# Banco de dados simples em memória
todos = []

# Listar todos os afazeres

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Criar novo o afazer

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = {
        'id': len(todos) + 1,
        'title': data.get('title'),
        'completed': False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# editar afazer específico
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = data.get('title', todo['title'])
            todo['completed'] = data.get('completed', todo['completed'])
            return jsonify(todo)
    return jsonify({'error': 'Todo not found'}), 404

#Deletar afazer
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(debug=True)
