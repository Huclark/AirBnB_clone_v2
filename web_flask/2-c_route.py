#!/usr/bin/pyhton3
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


@app.route('/c/<text>', strict_slashes=False)
def take_text(text):
    """This route displays 'C ' followed by the value of the text variable
    replacing underscores with spaces.

    Args:
        text (str): The text to be displayed after 'C '

    Returns:
        str: 'C ' followed by the value of text with underscores replaced by
        spaces
    """
    return F"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
