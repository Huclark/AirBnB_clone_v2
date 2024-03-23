#!/usr/bin/python3
"""This script starts a Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def teardown(self):
    """Removes the current session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a page with a list of all State objects"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a page which lists all cities linked to a state"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
