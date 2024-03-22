#!/usr/bin/python3
"""This script starts a Flask web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_route():
    """This is the root route

    Returns:
        str: returns 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """This route displays HBNB

    Returns:
        str: HBNB
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
