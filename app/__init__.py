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


@app.before_first_request
def before_first_request():
    print('앱 가동 후 첫번째 요청 전에 호출')


@app.before_request
def before_request():
    print('매 요청 전 호출')


@app.after_request
def after_request(response):
    print('매 요청 처리 후 호출')
    return response


@app.teardown_request
def teardown_request(exception):
    print('요청 결과를 브라우저에 응답한 후 호출')


@app.teardown_appcontext
def teardown_appcontext(exception):
    print('HTTP 요청의 애플리케이션 컨텍스트가 종료될 때 호출')

