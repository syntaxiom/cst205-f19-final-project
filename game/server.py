# ----
# Init
# ----

from flask import Flask, render_template, jsonify, request
import json
import datetime

app = Flask(__name__)

# ------
# Models
# ------

class Route:
    def __init__(self, title):
        self.title = title

class File:
    def __init__(self, name, hide_extension=False):
        dots = name.split('.')
        
        if hide_extension:
            self.name = dots[0]
        else:
            self.name = name
            
        self.extension = name.split('.')[-1]

class Desktop(Route):
    def __init__(self, title, files, icon_size):
        Route.__init__(self, title)
        self.files = files
        self.icon_size = icon_size

class Pdf(Route):
    def __init__(self, title, content):
        Route.__init__(self, title)
        self.content = content

class Message:
    def __init__(self, subject, date, content, author):
        self.subject = subject
        self.date = date
        self.content = content
        self.author = author

class Email(Route):
    def __init__(self, message):
        Route.__init__(self, "Emily's email")
        self.message = message

class Entry:
    def __init__(self, subject, content):
        self.subject = subject
        self.content = content

class Diary(Route):
    def __init__(self, entry):
        Route.__init__(self, "Emily's diary")
        self.entry = entry

# ----
# Data
# ----

real_birthday_email = "lauren<3.email"
real_exs_name_diary = "feb_14_2019.diary"

fake_birthday_diary = "apr_19_2019.diary"
fake_exs_name_diary = "dec_09_2019.diary"

# ------
# Routes
# ------

routes = {
    '/': Desktop(
        'Point-and-hack',
        [
            File('about.pdf'),
            # File('Email.email', True),
            File(real_birthday_email),
            # File('Diary.diary', True)
            File(real_exs_name_diary),
            File(fake_birthday_diary),
            File(fake_exs_name_diary)
        ],
        '48px'
    ),
    
    '/about.pdf': Pdf(
        'About this game',
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
    ),
    
    # Emails
    
    f"/{real_birthday_email}": Email(
        # real birthday
        Message(
            "Belated happy birthday!",
            datetime.datetime(2019, 7, 22, 13, 37),
            "Hi, Emily. It's Lauren. Belated Happy Birthday! I do not know how I missed your birthday, but I hope it was a good one and that you enjoyed your special party last night. Best wishes for the coming year. Belated Happy Birthday. With Love, Lauren",
            "lauren1992@jmail.com"
        ),
    ),
    
    #  Diaries
    
    f"/{real_exs_name_diary}": Diary(
        Entry(
            "February 14, 2019",
            "Today felt like the longest day of my life. I knew it would be, because I've had the Computer Science and Art History midterms marked in my calendar for weeks, plus it's Valentine's Day, and with everything that happened with Peter last month I knew any mention of the word \"love\" would make me want to throw up..."
        )
    ),
    f"/{fake_birthday_diary}": Diary(
        Entry(
            "April 19, 2019",
            """The party was hella fun. I cannot believe that I met all of my friends again after a long time. They were asking about me and Josh. I just smiled. I enjoyed this day so far."""
        )
    ),
    f"/{fake_exs_name_diary}": Diary(
        Entry(
            "December 9, 2019",
            """It's been a while. I saw him again at the mall today. I said 'hey Dan'. He said hi back to me. We talked for 30 minutes. Then I had to leave for a meeting. He asked me to meet up again if we have some free time. I was happy that I got to see him
            again after a long time."""
        )
    ),
    
    #real dog
    '/roo.png': {
        'static_path': '/pets/roo.png'
    },

    #red herring
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
    
    #fake exs photos
    '/old_memory_David.png': {
        'static_path': 'exs/old_memory_David.png'

    },
    '/fun_time_with_Ken.png':{
        'static_path':'exs/fun_time_with_Ken.png'
    },
    
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
    name = name.lower()
    return render_template(name + '.html', my_data=routes['/' + name])