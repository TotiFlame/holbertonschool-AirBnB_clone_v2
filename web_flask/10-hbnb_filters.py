#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def removesql(exit):
    """
    It removes the SQLite database file
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnbfilters():
    """
    It renders the template 10-hbnb_filters.html,
    passing it the states and amenities objects
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
