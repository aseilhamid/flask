from flask import Flask
from werkzeug.urls import quote

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!, THis is python flask app using DevOps Tools'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

