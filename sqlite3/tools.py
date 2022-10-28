from flask import Flask , jsonify , request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
host = '0.0.0.0'
port = 5000
           #show         regis       delete      edit   
url = {"/","/robot_show","robot_add","robot_del","robot_edit"}
path = "./db.sqlite"
class TEXT :
  def Document() -> str:
    table = []
    for i in url :
      table.append(i)
    return table


def sql_cli(data) :
  with sqlite3.connect(path) as conn :
    conn.execute(data)    


class Sql :
  def add(data) -> str :
    name = data["name"]
    ip = data["ip"]
    cmd = f'insert into db(name,ip)values("{name}","{ip}");'
    sql_cli(cmd)
    return {"status":"Add success"}

  def delete(data) -> str :    
    id = data["id"]
    cmd = f'delete from db where id="{id}";'
    sql_cli(cmd)
    return {"status":"Delete success"}

  def edit(data) -> str :    
    id = data["id"]
    name = data["name"]
    ip = data["ip"]

    cmd = f'update db set name="{name}" , ip="{ip}" where id={id};'
    sql_cli(cmd)
    return {"status":"Update success"}


  def show(data) -> str :
    with sqlite3.connect(path) as conn :
      cmd = f'select * from db;'
      table = []
      for i in conn.execute(cmd):
        table.append({"id":i[0],"name":i[1],"ip":i[2]})
      return table


class SERVER :
  def Run():
    app.run(host,port)




