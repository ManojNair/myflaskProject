from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return f"{os.environ['Cloud']} is awesome!!!!"


if __name__ == '__main__':
    app.run()
