from flask import Flask
import requests
import json
import facebook

#Import App ID and App Secret from Config file
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('secret.cfg')

#
class facebook_job(object):
    """"
    def login(fb_app_id):
        url = 'https://graph.facebook.com/dialog/outh?client_id='\
            + fb_app_id + '&redirect_url=http://localhost:5000/next'
        resp = json.loads(requests.get(url).content)
        app_access_token = resp['access_token']
        return app_access_token
    """
    # Set Perametar
    def __int__(self, app_id, app_secret):
        print (self.app_id)


    # Get Code
    """"
    def login(self):
        url = 'https://www.facebook.com/v9.0/dialog/oauth?client_id='\
            + self.app_id + '&redirect_uri=http://profilelink.biz'
        print(url)
        resp = requests.get(url)
        json = requests.get(url).content
        print(json)
"""

#FB_APP_ACCESS_TOKEN = login(FB_APP_ID)
#print (app.config['FB_APP_ID'])
FB_APP_ID = app.config['FB_APP_ID']
FB_APP_SECRET = app.config['FB_APP_SECRET']
fb_job = facebook_job()
fb_job.__int__(FB_APP_ID, FB_APP_SECRET)
