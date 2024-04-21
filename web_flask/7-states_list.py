#!/usr/bin/python3
"""using Flask to display our HBNB data,
you will need to update some part of our engine"""

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page"""
    sorted_list = sorted(storage.all(State).values(), key=lambda st: st.name)
    return render_template("7-states_list.html", sorted_states=sorted_list)


@app.teardown_appcontext
def terminate(exception):
    """close storage"""
    storage.close()


if __name__ == '__main__':
    """web application listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
