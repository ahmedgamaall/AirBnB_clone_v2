#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page like 6-index.html"""
    states_lt = storage.all("State").values()
    amenities_lt = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states_lt,
                           amenities=amenities_lt)


@app.teardown_appcontext
def teardown_db(exception):
    """close storage"""
    storage.close()

if __name__ == '__main__':
    """web application listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port='5000')
