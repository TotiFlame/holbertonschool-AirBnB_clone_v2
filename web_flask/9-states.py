#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def idlist(id=None):
    states = storage.all(State).values()
    st = None
    for i in states:
        if id == i.id:
            st = i
            break
    return render_template('9-states.html', states=states,
                           id=id, st=st)


@app.teardown_appcontext
def removesql(exit):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
