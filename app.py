from flask import Flask, render_template, request, session,url_for, redirect
import random
from flask.views import MethodView
import requests
import json
import facebook

app = Flask(__name__)

@app.route('/', methods = ['GET'])
class facebook_login:
    """"
    def login(fb_app_id):
        url = 'https://graph.facebook.com/dialog/outh?client_id='\
            + fb_app_id + '&redirect_url=http://localhost:5000/next'
        resp = json.loads(requests.get(url).content)
        app_access_token = resp['access_token']
        return app_access_token
    """
    def login(fb_app_id):
        url = 'https://www.facebook.com/v9.0/dialog/oauth?client_id='\
            + fb_app_id + '&redirect_url=http://localhost:5000/next'
        print(url)
        json = requests.get(url).content
        print(json)

    FB_APP_ID = '515948162695809'
    FB_APP_SECRET = '1474c603c3cb832ca8881746ad2c1805'
    FB_APP_ACCESS_TOKEN = login(FB_APP_ID)


"""
@app.template_filter('sum')
def sum_filter(data):
    total = 0
    for item in data:
        total += item
    return total

app.jinja_env.filters['sum'] = sum_filter
"""

@app.route('/post', methods = ['GET'])
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
