from flask import Flask , jsonify ,request
from flask_cors import CORS 
import sqlite3

app = Flask(__name__)


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
  
def SqlExcute(cmd,opt):
  try:
    db = sqlite3.connect('db.db')
    if opt == "create":
      db.execute(cmd)
      return ({"Status":"Success"})
    elif opt == "find":
      DataList = []
      data = db.execute(cmd)
      for i in data:
        print(i)
      return data
  except Exception as e:
    return ({"Status":"Fail"})
  
class Sql(Manage):
  def Create(self):
    cmd = f'create table {self.db_name}({db_target(self.db_raw)})'
    return SqlExcute(cmd,"create")

  def Find(self):
    cmd = f'select * from {self.db_name};'
    return SqlExcute(cmd,"find")

class Server :
  def Run():
    app.run()