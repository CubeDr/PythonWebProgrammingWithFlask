from flask import Flask, g
from flask import Response, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    c = getattr(g, 'c', 0)
    return 'Hello world! {}'.format(c)


@app.before_request
def increase_count():
    c = getattr(g, 'c', 0)
    g.c = c + 1


@app.route('/response/class')
def response_class():
    custom_response = Response('Custom Response', 200, {
        'Program': 'Flask Web Application'
    })
    return make_response(custom_response)


@app.route('/response/string')
def response_string():
    # return make_response('String response')
    return 'String response'


@app.route('/response/unicode')
def response_unicode():
    # return make_response(unicode('String response'))
    return u'String response'


@app.route('/response/wsgi')
def response_wsgi():
    def application(environ, start_response):
        response_body = 'The request method was %s' % environ['REQUEST_METHOD']

        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain'),
                            ('Content-Length', str(len(response_body)))]
        start_response(status, response_headers)

        return [response_body]

    return make_response(application)


@app.route('/response/tuple')
def response_tuple():
    return make_response(('Tuple Custom Response', 'OK', {
        'response_method': 'Tuple Response'
    }))
