from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

data = {
    'name': 'Dummy',
    'lucky_number': 42
}

routes = {
    'index': {
        'greeting': 'Hello, world!',
        'shopping_list': ['apple', 'orange', 'banana']
    },
    'about': {
        'message': 'This is the about page!'
    }
}

# Utilities
def bytesToDictionary(bytes):
    return json.loads(bytes.decode('utf8'))

# Routes
@app.route('/')
def index():
    return render_template('index.html', my_data=routes['index'])

@app.route('/about')
def about():
    return render_template('about.html', my_data=routes['about'])

# API
@app.route('/__api__/lucky_number')
def api_lucky_number():
    return jsonify(data['lucky_number'])

@app.route('/__api__/change_lucky_number', methods=['GET', 'POST'])
def api_change_lucky_number():
    req = bytesToDictionary(request.data)
    data['lucky_number'] = req['newNumber']
    return jsonify(data['lucky_number'])