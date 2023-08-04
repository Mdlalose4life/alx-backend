#!/usr/bin/env python3
""" basic Flask app in 1-app.py
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)


class Config(object):
    """instantiating the Babel object in the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """timezones
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
