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
        'files': [
            {
                'name': 'hello.txt',
                'extension': 'text'
            },
            {
                'name': 'about.pdf',
                'extension': 'pdf'
            },
            {
                'name': 'Email',
                'extension': 'email'
            }
        ]
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
    #real birthday
    '/email/22_Jul_2019.txt': {
        'content': "Hi, Emily. It's Lauren. Belated Happy Birthday! I do not know how I missed your birthday, but I hope it was a good one and that you enjoyed your special party last night. Best wishes for the coming year. Belated Happy Birthday. With Love, Lauren"
    },
    #real ex's name
    '/diary/14_Feb_2019.txt': {
        'content': "February 14, 2019 Today felt like the longest day of my life. I knew it would be, because I've had the Computer Science and Art History midterms marked in my calendar for weeks, plus it's Valentine's Day, and with everything that happened with Peter last month I knew any mention of the word \"love\" would make me want to throw up..."
    },
    
    #real dog
    '/roo.png': {
        'static_path': '/pets/roo.png'
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
        'content': """It's been a while. I saw her again at the mall today. I said 'hey Dan'. He said hi back to me. We talked for 30 minutes. Then I had to leave for a meeting. He asked me to meet up again if we have some free time. I was happy that I got to see him
         again after a long time. """
    },
    #fake exs photos
    '/old_memory_David.png': {
        'static_path': 'exs/old_memory_David.png'

    },
    '/fun_time_with_Ken.png':{
        'static_path':'exs/fun_time_with_Ken.png'
    },
    #fake birthday txt
    '/diary/19_April_2019.txt': {
        'content': """The party was hella fun. I cannot believe that I met all of my friends again after a long time. They were asking about me and Josh. I just smiled. I enjoyed this day so far."""
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