from flask import Flask, request, jsonify, logging
from flask import has_request_context, request, make_response
from flask.logging import default_handler
from urllib.parse import urlparse

import requests
import jsonify
import datetime
import logging
import os

app = Flask(__name__)

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)

formatter = RequestFormatter(
    '[%(asctime)s] %(message)s'
)


@app.before_request
def before_first_request():
    log_level = logging.INFO

    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)

    logdir = '/opt/logs'
    log_file = os.path.join(logdir, 'livecd.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)


#@app.route('/', methods=['GET'])
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def name(path):
    parsed_url = urlparse(request.url)
    message = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) + " " + parsed_url.path + " " + parsed_url.query + " " + parsed_url.fragment
    app.logger.info(message)
    response = make_response(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    response.headers['Server'] = 'HL'
    return(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

