#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states')
def states():
    """display a HTML page"""
    sorted_states = storage.all(State)
    return render_template("9-states.html",
                           sorted_states=sorted_states)


@app.route('/states/<id>')
def states_id(id):
    """display a HTML page"""
    stt = None
    not_found = True
    for state in storage.all(State).values():
        if state.id == id:
            stt = state
            not_found = False
            break
    return render_template("9-states.html", id=id,
                           state=stt, notfound=not_found)


@app.teardown_appcontext
def terminate(excep):
    """close storage"""
    storage.close()


if __name__ == '__main__':
    """web application listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
