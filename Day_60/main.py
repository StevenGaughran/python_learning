import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')
    return f"<h1>Name: {username}, Password: {password}</h1>"
    # return render_template("login.html", un=username, pw=password)


if __name__ == "__main__":
    app.run(debug=True)
