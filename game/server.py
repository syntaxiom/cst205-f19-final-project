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
        'files': ['hello.txt', 'about.pdf']
    },
    '/hello.txt': {
        'content': "Wait, don't look!"
    },
    '/about.pdf': { 
        'content': 
"""
# Point-and-hack

Crack the password! Er, the security questions to obtain the password! Why are we doing this again?

## Authors

Sean Lester-Wilson

YE LIN JOH

Quynh Nguyen

## Images

## Tools
"""
    },
    '/email': {
        'content': "Hi, Emily. It's Lauren. Belated Happy Birthday! I do not know how I missed your birthday , but I hope it was a good one and that you enjoyed your special day. Best wishes for the coming year. Belated Happy Birthday. With Love, Lauren"
    },
    '/diary/12_Nov_2019.txt': {
        'content': ""
    },
    
    #red herring
    '/discord_friends.png': {
        'static_path': '/nested/because/easy.png'
    },
    '/rex.jpeg': {
        'static_path': '/pets/rex.png'
    },
    '/dolly.jpeg': {
        'static_path': '/pets/max.png'
    },
    '/the_bestest_boy_max.png': {
        'static_path':'/pets/max.png'
    },
    '/lucy.png': {
        'static_path':'/pets/lucy.png'
    },
    '/my_little_angel_pie.png': {
        'static_path':'/pets/pie.png'
    },
    '/diary/9_Dec_2019.txt': {
        'content': "It's been a while. I saw her again at the mall today. I said 'hey Emma'. She said hi back to me. We talked for 30 minutes. Then I had to leave for a meeting. She asked me to meet up again if we have some free time. I was happy that I got to see her again after a long time. "
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