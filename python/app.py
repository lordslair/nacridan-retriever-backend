# -*- coding: utf8 -*-

from queries   import *
from functions import funct_greet
from flask     import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/greet')
def say_hello():
  return funct_greet()

@app.route('/pcs/id/<int:pcs_id>')
def send_pcs_info(pcs_id):
  result = query_pcs_id(pcs_id) # result will be a JSON
  if result:
    return result
  else:
    return '{}'
