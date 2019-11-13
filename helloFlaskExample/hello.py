from flask import Flask, render_template

app = Flask(__name__)

@app.route('/mytemplate')
def t_test():
	return render_template('template.html')