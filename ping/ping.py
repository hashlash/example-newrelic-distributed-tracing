import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

import requests
from flask import Flask

app = Flask('ping')

@app.route('/ping')
def ping():
    app.logger.info('ping')
    r = requests.get('http://localhost:5001/pong')
    return f'ping {r.text}'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
