from flask import Flask
import requests
import json
import facebook

#Import App ID and App Secret from Config file
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('secret.cfg')
