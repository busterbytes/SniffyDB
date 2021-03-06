from flask import Flask
import os

__author__ = "Donald Cha"

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = basedir + '/../../../pcaps'

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['pcap'])

from app import views
