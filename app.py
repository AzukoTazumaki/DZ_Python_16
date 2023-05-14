import os
from flask import Flask, render_template, request, redirect, json
from flask_socketio import SocketIO, send
from werkzeug.exceptions import BadRequest
import exercises

app = Flask(__name__)
secret_key = os.urandom(12)
app.config['SECRET_KEY'] = secret_key
socket_io = SocketIO(app)


@app.route('/')
def main_page():
    return render_template('main/index.html')


@app.route('/ex_1', methods=['POST', 'GET'])
def ex_1():
    ex_1_answer = exercises.common_divisor(request.form['gcd'])
    return redirect('/#gcd')


@app.route('/ex_3', methods=['POST', 'GET'])
def ex_3():
    if request.method == 'POST':
        knight = exercises.Knight()
        knight.knights_move(request.form['knights_move'])
        board_first_line = '\t|\t'.join([str(x) for x in knight.board[0]])
        board_second_line = '\t|\t'.join([str(x) for x in knight.board[1]])
        board_third_line = '\t|\t'.join([str(x) for x in knight.board[2]])
        board_fourth_line = '\t|\t'.join([str(x) for x in knight.board[3]])
        board_fifth_line = '\t|\t'.join([str(x) for x in knight.board[4]])
        board_sixth_line = '\t|\t'.join([str(x) for x in knight.board[5]])
        return render_template('main/ex_3_answer.html',
                               board_first_line=board_first_line,
                               board_second_line=board_second_line,
                               board_third_line=board_third_line,
                               board_fourth_line=board_fourth_line,
                               board_fifth_line=board_fifth_line,
                               board_sixth_line=board_sixth_line)
    return redirect('/#knight_move')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return render_template('errors/bad_request.html'), 400


if __name__ == '__main__':
    socket_io.run(app, debug=True)
