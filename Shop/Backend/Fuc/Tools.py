from flask import Flask , jsonify ,request
from flask_cors import CORS 

import sqlite3

db = sqlite3.connect('db.db')
app = Flask(__name__)


class Manage :
  def __init__(self,data) -> None:
     self.db_name = data['db_name']
     self.db_target = data['db_target']
  
class Sql :
  def __init__(self,data) -> None:
    self.data = data
    
  def Create(self):
    print(self.data)
    
  


class Server :
  def Run():
    app.run()