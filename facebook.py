from flask import Flask
import requests
import json
import facebook

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('secret.cfg')

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

    FB_APP_ID = app.config['FB_APP_ID']
    FB_APP_SECRET = app.config['FB_APP_SECRET']
    #sFB_APP_ACCESS_TOKEN = login(FB_APP_ID)
