"""portfolio index (main) view.

URLs include:
/
"""
# from types import MethodDescriptorType
from os import path
import flask
from flask import send_from_directory
from flask.helpers import url_for
import portfolio


# Helper Functions
# ====================================================


@portfolio.app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    """Fetch file from uploads directory."""
    logname = get_logname()
    if logname is None:
        flask.abort(403)
    if not path.isfile(portfolio.app.config['UPLOAD_FOLDER']/filename):
        flask.abort(404)
    return send_from_directory(portfolio.app.config['UPLOAD_FOLDER'], filename)


@portfolio.app.route('/images/<filename>', methods=['GET'])
def static_image(filename):
    """Render (and possibly caches) static image file."""
    return send_from_directory('static/images', filename)


@portfolio.app.route('/js/<filename>', methods=['GET'])
def script(filename):
    """Fetch script for index render with caching."""
    return send_from_directory('js', filename)


def get_logname():
    """Get the currently logged in user or returns None if not logged in."""
    if 'username' in flask.session:
        user = flask.session['username']
        return user
    return None


# Main Index Page
# ====================================================


@portfolio.app.route('/')
def show_index():
    """Display / route."""
    context = {
    }
    return flask.render_template("index.html", **context)
