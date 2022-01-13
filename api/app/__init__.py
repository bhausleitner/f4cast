from flask import Flask

import sys
sys.path.append('..')
  
from config import Config

app = Flask(__name__ ,static_folder='../../build',static_url_path='')
app.config.from_object(Config)

from app import routes




