from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>/')
def user(name):
    return render_template('index.html', content=name)


@app.route('/')
def home():
	return 'Home Page'

@app.route('/error/')
def error():
    return 'Error 404'

if __name__ == '__main__':
    app.run(debug=True)
