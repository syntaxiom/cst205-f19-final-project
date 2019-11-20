from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])