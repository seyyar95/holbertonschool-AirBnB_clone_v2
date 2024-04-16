#!/usr/bin/python3

"""Module that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display State, City, Amenity"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
