from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []  # List to store to-do items

@app.route('/todosl', methods=['POST'])
def add_todo():
    data = request.get_json()
    if 'title' not in data:
        return jsonify({'error': 'Title is required'})

    todo_id = len(todos) + 1
    todo = {'id': todo_id, 'title': data['title'], 'completed': data.get('completed', False)}
    todos.append(todo)
    return jsonify(todo)

@app.route('/todosl', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todosl/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    todo = next((todo for todo in todos if todo['id'] == id), None)
    if not todo:
        return jsonify({'error': 'To-do item not found'})
    return jsonify(todo)

@app.route('/todosl/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((todo for todo in todos if todo['id'] == id), None)
    if not todo:
        return jsonify({'error': 'To-do item not found'})

    data = request.get_json()
    if 'title' in data:
        todo['title'] = data['title']
    if 'completed' in data:
        todo['completed'] = data['completed']

    return jsonify(todo)

@app.route('/todosl/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todo = next((todo for todo in todos if todo['id'] == id), None)
    if not todo:
        return jsonify({'error': 'To-do item not found'})

    todos = [todo for todo in todos if todo['id'] != id]
    return jsonify({'message': 'To-do item deleted'})

if __name__ == '__main__':
    app.run(debug=True)
