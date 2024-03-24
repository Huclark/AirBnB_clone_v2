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


@app.route('/states', strict_slashes=False)
def states_list():
    """Displays a page with a list of all State objects"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displays a page whiche lists all cities linked to a stat"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
