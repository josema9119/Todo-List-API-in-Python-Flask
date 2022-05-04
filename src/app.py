from flask import Flask, jsonify
app = Flask(__name__)
from flask import jsonify
from flask import request
import json

todos =[
     { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decode_object = json.loads(request_body)
    todos.append(decode_object)
    json_text = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    return 'something'
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)