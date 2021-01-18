from flask import Flask, render_template, request, session,url_for, redirect
from flask.views import MethodView
import requests
import json
import config
import facebook
import facebook_link

app = Flask(__name__)

# Create new secret_key
app.secret_key = config.randomCharacter(16)

# Login Page Access
@app.route('/login', methods = ['GET'])
def login():
    return render_template('login.html',\
                            title = 'Login',\
                            err = False,\
                            message = 'Plese enter your Email Address and Password',\
                            email = ''
                            )
# Login Form Send
@app.route('/login', methods = ['POST'])
def login_post():
    email = request.form.get('email')
    pwd = request.form.get('password')
    session['state'] = app.secret_key
    if session['state']:
        return redirect('/')
    else:
        return render_template('login.html',\
                                title = 'Login',\
                                err = False,\
                                message = 'Plese enter again',\
                                email = email
                                )

# Get Input Values from Post Page
@app.route('/', methods = ['GET'])
def form_get():
    if 'state' in session and session['state']:
        return render_template('post.html',
                                title = "Post Page",
                                message = "以下の欄を入力してください"
                                )
    else:
        redirect ('/login')

"""
# Post Input Values to each Profile
@app.route('/', methods = ['POST'])
def form_post():
    # Get "checkbox" Values from Form
    ############################################################
    ##  IF Add post.html "checkbox" value, Add Values  below  ##
    ############################################################
    fb = request.form.get('fb')
    ig = request.form.get('ig')
    ta = request.form.get('ta')

    # Set global Valuables from Form
    global INPUT_NAME
    global INPUT_ADDRESS
    global INPUT_PHONE

    INPUT_NAME = "test" #request.form.get('input_name')
    INPUT_ADDRESS =  "test" #request.form.get('input_address')
    INPUT_PHONE =  "00000000000" #request.form.get('input_phone')

    ############################################
    ##  Divided Case by post.html "checkbox"  ##
    ############################################

    ############################################################
    ##  IF Add post.html "checkbox" value, Add mldules below  ##
    ############################################################

    # Facebook_link.py Run!!
    if fb = True:
        facebook_link(INPUT_NAME, INPUT_ADDRESS, INPUT_PHONE)
    else pass

    # Instagram_link.py Run!!
    if ig = True:
        Instagram_link(INPUT_NAME, INPUT_ADDRESS, INPUT_PHONE)
    else pass

    # Tripadvisor_link.py Run!!
    if ta = True:
        Tripadvisor_link(INPUT_NAME, INPUT_ADDRESS, INPUT_PHONE)
    else pass

"""

"""
#logout
@app.route('/logout', methods = ['POST'])
def logout():
    session.pop('id', None)
    session.pop('login')
    return redirect9('/login')
"""
#app.secret_key = b'testtesttest'

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
