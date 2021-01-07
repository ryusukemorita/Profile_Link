from flask import Flask, render_template, request, session,url_for, redirect
import random
from flask.views import MethodView
import requests
import json
import facebook

app = Flask(__name__)

@app.route('/', methods = [])
def


# Login page access
@app.route('/login', methods = ['GET'])
def login():
    return render_template('login.html',\
                            title = 'Login',\
                            err = False,\
                            message = 'Plese enter your Email Address and Password',\
                            email = ''
                            )
# Login form sended
@app.route('/login', methods = ['POST'])
def login_post():
    return render_template('login.html'\
                            title = 'login''\
                            )

@app.route('/', methods = ['GET'])
def post():
    return render_template('post.html',
                            title = "Post Page",
                            message = "以下の欄を入力してください"
                            )


#secret_keyにランダムなbyte文字列を設定する
app.secret_key = b'testtesttest'

class HelloAPI(MethodView):
    send = ''

    def get(self):
        if 'send' in session:
            msg = 'send' + session['send']
            send = session['send']
        else:
            msg = 'write something'
            send = ''
        return render_template('next.html', title = 'Next Page',
                               message = msg,
                               send = send )

    def post(self):
        session['send'] = request.form['send']
        return redirect('/')

#ßapp.add_url_rule('/hello/', view_func = HelloAPI.as_view('hello'))

"""
# Post Method
@app.route('/', methods = ['POST'])
def form():
    ck = request.form.get('check')
    rd = request.form.get('radio')
    sel = request.form.getlist('sel')
    return render_template('index.html',
                            title="index with Jinja",
                            message = [ck, rd, sel])
"""

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
