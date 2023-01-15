# __winc_id__ = "cc1b724762854e85a8defa04287f708b"
# __human_name__ = "requests"

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p> Home, sweet home.</p>"


@app.route("/greet")
def greet():
    return "<h1>Hello, world!</h1>"


@app.route("/greet/<example_name>")
def greet_name(example_name):
    return "<h1>Hello, {}!</h1>".format(example_name)


if __name__ == "__main__":
    app.run()

# Terminal:
# export FLASK_APP=main.py
# flask run
