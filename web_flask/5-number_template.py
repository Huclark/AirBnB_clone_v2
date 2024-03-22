#!/usr/bin/python3
"""This script starts a Flask web app"""
from flask import Flask, abort, render_template

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
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text="is cool"):
    """This route displays 'Python ' followed by the value of the text variable
    replacing underscores with spaces.

    Args:
        text (str, optional): The text to be displayed after 'Python '.
        Defaults to "is cool".

    Returns:
        str: 'Python ' followed by the value of text with underscores replaced
        by spaces.
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def python_number(n):
    """This route checks if n is a number and displays a string if
    n is a number

    Args:
        n (str): the number to check

    Returns:
        str: a string
    """
    return f"{n} is a number" if n.isdigit() else abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def we_dey_render(n=None):
    """This route checks if n is a number and renders an html page if
    n is a number

    Args:
        n (str): the number to check
    """
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
