# ----
# Init
# ----

from flask import Flask, render_template, jsonify, request
import json
import datetime
import random

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

# ------------
# Route models
# ------------

class Desktop(Route):
    def __init__(self, title, files, icon_size):
        Route.__init__(self, title)
        self.files = files
        self.icon_size = icon_size

# -----------
# File models
# -----------

class PDF(File):
    def __init__(self, name, content):
        File.__init__(self, name)
        self.content = content

class Email(File):
    def __init__(self, name, subject, date, content, author):
        File.__init__(self, name)
        self.subject = subject
        self.date = date
        self.content = content
        self.author = author

class Diary(File):
    def __init__(self, name, subject, content):
        File.__init__(self, name)
        self.subject = subject
        self.content = content

class Picture(File):
    def __init__(self, name, url):
        File.__init__(self, name)
        self.url = f"static/{url}"
        
# ----
# Data
# ----

real_birthday_email = "lauren<3.email"

real_exs_name_diary = "feb_14_2019.diary"
fake_birthday_diary = "apr_19_2019.diary"
fake_exs_name_diary = "dec_09_2019.diary"

# -----
# Files
# -----

PDFs = [
    PDF(
        'about.pdf',
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
]

emails = [
    Email(
        real_birthday_email,
        "Belated happy birthday!",
        datetime.datetime(2019, 7, 22, 13, 37),
        "Hi, Emily. It's Lauren. Belated Happy Birthday! I do not know how I missed your birthday, but I hope it was a good one and that you enjoyed your special party last night. Best wishes for the coming year. Belated Happy Birthday. With Love, Lauren",
        "lauren1992@jmail.com"
    ),
]

diaries = [
    Diary(
        real_exs_name_diary,
        "February 14, 2019",
        "Today felt like the longest day of my life. I knew it would be, because I've had the Computer Science and Art History midterms marked in my calendar for weeks, plus it's Valentine's Day, and with everything that happened with Peter last month I knew any mention of the word \"love\" would make me want to throw up..."
    ),
    Diary(
        fake_birthday_diary,
        "April 19, 2019",
        """The party was hella fun. I cannot believe that I met all of my friends again after a long time. They were asking about me and Josh. I just smiled. I enjoyed this day so far."""
    ),
    Diary(
        fake_exs_name_diary,
        "December 9, 2019",
        """It's been a while. I saw him again at the mall today. I said 'hey Dan'. He said hi back to me. We talked for 30 minutes. Then I had to leave for a meeting. He asked me to meet up again if we have some free time. I was happy that I got to see him
        again after a long time."""
    ),
]

pictures = [
    Picture('fun_time_with_Ken.png', 'exs/Ken.png'),
    Picture('old_memory_David.png', 'exs/David.png'),
    Picture('rex.png', 'pets/rex.png'),
    Picture('roo.png', 'pets/roo.png'),
    Picture('dolly.png', 'pets/max.png'),
    Picture('max.png', 'pets/max.png'),
    Picture('lucy.png', 'pets/lucy.png')
]

files = []
files.extend(PDFs)
files.extend(emails)
files.extend(diaries)
files.extend(pictures)
files.append(File('secret.zip'))

# ----------
# Route data
# ----------

routes = {
    '/': Desktop(
        'Point-and-hack',
        random.sample(files, len(files)),
        '48px',
    )
}

for file in files:
    routes[f"/{file.name}"] = file

# ---------
# Utilities
# ---------

def bytesToDictionary(bytes):
    return json.loads(bytes.decode('utf8'))

# ------
# Routes
# ------

@app.route('/')
def index():
    return render_template('index.html', my_data=routes['/'])
    
@app.route('/<name>')
def dynamo(name):
    return render_template(name + '.html', my_data=routes['/' + name])

@app.route('/api/guess', methods=['POST'])
def guess():
    req = bytesToDictionary(request.data)
    return jsonify(req)