from flask import Flask , jsonify ,request
from flask_cors import CORS 

import sqlite3

db = sqlite3.connect('db.db')
app = Flask(__name__)
class Manage :
  def __init__(self ,data) -> None:
    self.db_name = str(data['db_name'])
    self.db_raw = str(data['db_raw']).split(",")

class Sql(Manage) :
  def __init__(self) -> None:
    print("1223123")
  def Create(self):
    print("123","<---- here")
    
    
class Server :
  def Run():
    app.run()