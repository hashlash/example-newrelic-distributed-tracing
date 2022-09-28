from flask import Flask

app = Flask('pong')

@app.route('/pong')
def pong():
    return 'pong'

if __name__ == '__main__':
    app.run(port=5001, debug=True)
