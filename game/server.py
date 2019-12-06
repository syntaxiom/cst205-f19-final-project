# ----
# Init
# ----

from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# ----
# Data
# ----

routes = {
    '/': {
        'greeting': 'Goodbye...',
        'files': ['hello.txt', 'pet.jpg', 'passwords.pdf']
    },
    '/hello.txt': {
        'content': "Wait, don't look!"
    }
}

# ---------
# Utilities
# ---------

def bytesToDictionary(bytes):
    return json.loads(bytes.decode('utf8'))

# ------
# Routes
# ------

# Index (home) route
@app.route('/')
def index():
    return render_template('index.html', my_data=routes['/'])
    
# Dynamic route
@app.route('/<name>')
def dynamo(name):
    return render_template(name + '.html', my_data=routes['/' + name])