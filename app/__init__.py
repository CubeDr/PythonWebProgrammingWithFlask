from flask import Flask, g

app = Flask(__name__)


@app.route('/')
def hello_world():
    c = getattr(g, 'c', 0)
    return 'Hello world! {}'.format(c)


@app.before_request
def increase_count():
    c = getattr(g, 'c', 0)
    g.c = c + 1
