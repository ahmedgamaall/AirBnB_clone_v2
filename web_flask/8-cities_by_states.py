#!/usr/bin/python3
""" a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a HTML page"""
    sorted_list = sorted(storage.all(
        State).values(), key=lambda st: st.name)
    for sl in sortedlist:
        sl.cities.sort(key=lambda ct: ct.name)
    return render_template("8-cities_by_states.html", sorted_states=sorted_list)


@app.teardown_appcontext
def terminate(excep):
    """close storage"""
    storage.close()


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)
