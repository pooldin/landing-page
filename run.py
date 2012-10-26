import os
from flask import Flask, send_from_directory

app = Flask(__name__)
root = os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def index():
    return send_from_directory(root, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            use_debugger=True,
            use_reloader=True)
