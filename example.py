from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/<name>/')
def user(name):
    return render_template('index.html', content=name)



@app.route('/')
def home():
	return render_template('home.html')

@app.route('/error/')
def error():
    return 'Error 404'

if __name__ == '__main__':
    app.run(debug=True)
