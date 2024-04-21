#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def states_and_state(id=None):
    """display a HTML page"""
    sorted_list = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    if id is None:
        return render_template("9-states.html", sorted_states=sorted_list,
			       hasStates=True)
    else:
        for sl in sorted_list:
            if sl.id == id:
                sl.cities.sort(key=lambda x: x.name)
                return render_template("9-states.html", state=sl)
    return render_template("9-states.html")


@app.teardown_appcontext
def terminate(exc):
    """close storage"""
    storage.close()


if __name__ == '__main__':
    """web application listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
