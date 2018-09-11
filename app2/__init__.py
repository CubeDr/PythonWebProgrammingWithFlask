from flask import Flask, request

app = Flask(__name__)


@app.route('/single_method', methods=['GET'])
def single_method_get():
    return 'single GET'


@app.route('/single_method', methods=['POST'])
def single_method_post():
    pass


@app.route('/multi_method', methods=['GET', 'POST'])
def multi_method():
    if request.method == 'GET':
        return 'multi GET'
    else:
        pass


@app.route('/argument/int/<int:num>')
def argument_int(num):
    return str(num*num)


@app.route('/argument/float/<float:num>')
def argument_float(num):
    return str(round(num))


@app.route('/argument/path/<path:p>')
def argument_path(p):
    return p
