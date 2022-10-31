from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Users route"

@app.route("/users")
def users():
    return render_template('users/index.html', users=["xdelltog"])

@app.route("/users/<string:name>")
def user(name):
    return f"User {name} route"