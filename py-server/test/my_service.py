import os
import sys
import redis
import socket
from contextlib import closing
from flask import redirect, url_for, render_template, Flask, request, jsonify

app = Flask('py-server')

@app.before_request
def before_request_func():
    if request.method == 'POST':
        r.incr('counter')

@app.after_request
def after_request_func(response):
    if request.method == 'GET':
        counter_key_val = {'counter': r.get('counter').decode('utf-8')}
        resp_json = response.get_json()
        if resp_json is None:
            resp_json = {}
        resp_json.update(counter_key_val)
        return jsonify(resp_json)

    return response

@app.route('/index', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def index():
    return 'Welcome to my Python Webservice'

@app.route('/counter', methods=['GET','POST'])
def handle_counter():
    return 'The counter is: {0}'.format(r.get('counter').decode('utf-8'))

@app.route('/<path:path>', methods=['GET','POST'])
def catch_all(path):
    return index()

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        print('Please use an integer between 1 to 65535 as port')
        sys.exit(1)
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex(('127.0.0.1', port)) == 0:
            print('Port {0} is already in use, exiting...'.format(port))
            sys.exit(1)
    r = redis.Redis(db=os.environ['db'])
    if r.exists('counter') == 0:
        r.set('counter', 0)
    app.run(host= '0.0.0.0',port=port)

