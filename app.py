import os
from flask import Flask, render_template, request, redirect, json
from flask_socketio import SocketIO, send
from werkzeug.exceptions import BadRequest
from exercises import *

app = Flask(__name__)
secret_key = os.urandom(12)
app.config['SECRET_KEY'] = secret_key
socket_io = SocketIO(app)


@app.route('/')
def main_page():
    return render_template('main/index.html')


@app.route('/ex_1', methods=['POST', 'GET'])
def ex_1():
    if request.method == 'POST':
        ex_1_answer = common_divisor(request.form['gcd'])
        socket_io.send(ex_1_answer)
    return redirect('/#gcd')


@socket_io.on('message')
def handle_message(data):
    print('received message: ' + json.dumps(data))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return render_template('errors/bad_request.html'), 400


if __name__ == '__main__':
    socket_io.run(app, debug=True)
