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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number", strict_slashes=False)
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    """ display a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Number: n is even|odd” inside the tag BODY"""
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == '__main__':
    """web application that listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)

