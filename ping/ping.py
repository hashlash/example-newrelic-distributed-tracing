import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask('ping')
CORS(app)

@app.route('/ping')
def ping():
    app.logger.info('ping')
    app.logger.debug(request.headers)
    r = requests.get('http://localhost:5001/pong')
    return f'ping {r.text}'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
