from flask import Flask
from flask import jsonify

import flask 

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Flask! Basics'

@app.route('/api/greet', methods=['GET'])
def get_request():
    greeting_message = {"message": "Hello World!"}
    return jsonify(greeting_message)

@app.route('/api/greet/<name>', methods=['GET'])
def custom_get_request():
    custom_greeting_message = {"message": f"Hello, {name}!"}
    return jsonify(custom_greeting_message)

if __name__ == '__main__':
    app.run(debug=True)
