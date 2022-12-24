from flask import Flask , jsonify ,request
from flask_cors import CORS 
import sqlite3

app = Flask(__name__)

def SqlExcute(cmd):
    db = sqlite3.connect('db.db')
    db.execute(cmd)
class Manage :
  def __init__(self ,data) -> None:
    self.db_name = str(data['db_name'])
    self.db_raw = str(data['db_raw']).split(",")

def db_type(raw):
  if raw == "id" : return f'{raw} integer primary key'
  elif raw == "unit" or raw == "price" : return f'{raw} string'
  else : return f'{raw} string'

def db_target(raw) -> str:
    cmd = ""
    for i in raw :
      if raw[len(raw) - 1] == i : cmd = cmd + f'{db_type(str(i))}'
      else :cmd = cmd + f'{db_type(str(i))},'
    return cmd

class Sql(Manage):
  def Create(self):
    cmd = f'create table {self.db_name}({db_target(self.db_raw)})'
    SqlExcute(cmd)
class Server :
  def Run():
    app.run()