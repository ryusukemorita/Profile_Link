from flask import Flask
import string, random

app = Flask(__name__)

def randomCharacter(n):
    c = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(c) for i in range(n)])
