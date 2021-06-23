"""portfolio package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (portfolio/config.py)
app.config.from_object('portfolio.config')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/config/
app.config.from_envvar('portfolio_SETTINGS', silent=True)

import portfolio.api  # noqa: E402  pylint: disable=wrong-import-position
import portfolio.views  # noqa: E402  pylint: disable=wrong-import-position
