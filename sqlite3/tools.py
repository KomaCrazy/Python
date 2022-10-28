from flask import Flask , jsonify , request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
host = '0.0.0.0'
port = 5000
           #show         regis       delete      edit   
url = {"/","/robot_show","robot_add","robot_del","robot_edit"}

class TEXT :
  def Document() -> str:
    table = []
    for i in url :
      table.append(i)
    return table

class Sql :
  def add(data) -> str :
    table = []
    name = data["name"]
    ip = data["name"]
    with sqlite3.connect("./db.sqlite") as conn :
      cmd = f'insert into db(name,ip)values("{name}","{ip}");'
      conn.execute(cmd)

      
class SERVER :
  def Run():
    app.run(host,port)




