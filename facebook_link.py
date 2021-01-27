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
    app_id = app.config['FB_APP_ID']
    app_secret = app.config['FB_APP_SECRET']


    # Get Code
    def login(self):
        url = 'https://www.facebook.com/v9.0/dialog/oauth?client_id='\
            + self.app_id + '&redirect_uri=https://profilelink.biz&state=' #+ app.secret_key
        print (url)
        #resp = requests.get(url)
        #json = requests.get(url).content
        #print(json)
        #code =
        #return code
"""
    # Get App Access Token
    def get_AccessToken(self):
        url = 'https://graph.facebook.com/v9.0/oauth/access_token?client_id='\
            + self.app_id + '&redirect_uri=https://profilelink.biz&client_secret=' + self.app_secret\
            + '&code=' + login.code    #入力
        resp = requests.get(url)
        json = requests.get(url).content
        access_token = json.

    # Manage Profile
    def manage_profile(self):
        graph = facebook.GraphAPI(access_token="self.access_token")
        accounts = graph.get_object(parent_object = 'me', connection_name = 'accounts')
        resp_obj = json.load(accounts)

        page_ids = []
        page_ids = resp_obj[account][data][id]

        # Set Values from Form
        input_value = [name: INPUT_NAME, address:INPUT_ADDRESS, phone: INPUT_PHONE]

        for page in page_ids:
            input_name = graph.put_object(parent_object = page, connection_name = name)
            input_address = graph.put_object(parent_object = page, connection_name = single_line_address)
            input_phone = graph.put_object(parent_object = page, connection_name = phone)
        
"""

#FB_APP_ACCESS_TOKEN = login(FB_APP_ID)
#print (app.config['FB_APP_ID'])
#FB_APP_ID = app.config['FB_APP_ID']
#FB_APP_SECRET = app.config['FB_APP_SECRET']
fb_job = facebook_job()#FB_APP_ID, FB_APP_SECRET)
fb_job.login
