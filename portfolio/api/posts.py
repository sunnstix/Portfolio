"""REST API for posts."""
import flask
from flask import request, session, jsonify
from flask.helpers import make_response, url_for
from flask import abort
import json
import portfolio


# Helpers
# ====================================================

def get_logname():
    """Get the currently logged in user or returns None if not logged in."""
    if 'username' in flask.session:
        user = flask.session['username']
        return user
    abort(403)


@portfolio.app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'message': 'Bad Request', 'status_code': 400}), 400)


@portfolio.app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'message': 'Forbidden', 'status_code': 403}), 403)


@portfolio.app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message': 'Not Found', 'status_code': 404}), 404)


def no_content():
    response = make_response('', 204)
    response.mimetype = portfolio.app.config['JSONIFY_MIMETYPE']
    return response

# REST API
# ====================================================


@portfolio.app.route('/api/v1/', methods=['GET'])
def fetch_resources():
    """Return API resource URLS."""
    return flask.jsonify(**{
        'posts': '/api/v1/p/',
        'url': '/api/v1/'
    })
