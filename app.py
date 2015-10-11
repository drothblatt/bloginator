from flask import Flask, render_template, session

import sqlite3

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/login")
@app.route("/login/")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
