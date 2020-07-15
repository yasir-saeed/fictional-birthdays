from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/<name>/")
def user(name):
	return f" <h1>{name}.</h1><br/> <b> Birthday: <b/> <br/> <b> Age: <b/>"

@app.route("/error/")
def error():
	return "error 404 page :/"


if __name__ == "__main__":
	app.run(debug = True)


