import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

from flask import Flask, request

app = Flask('pong')

@app.route('/pong')
def pong():
    app.logger.info('pong')
    app.logger.debug(request.headers)
    return 'pong'

if __name__ == '__main__':
    app.run(port=5001, debug=True)
