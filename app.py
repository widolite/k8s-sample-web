from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello K8s!'


if __name__ == '__main__':
    app.run()
