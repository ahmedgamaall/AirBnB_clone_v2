#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Route /"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route /hbnb"""
    return "HBNB"


if __name__ == '__main__':
    """web application that listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
