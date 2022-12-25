from flask_cors import CORS
from flask import Flask , jsonify , request
import sqlite3 

app = Flask(__name__)
CORS(app)


class Sql :
  def Find(x):
    pass
    
class Manage:
  def __init__(self,table) -> None:
    self.table = table["table"]
    self.field = table["field"]

class Sql(Manage):
  def       
    

class Server :
  def Run():
      app.run('0.0.0.0',5000)
  
  
  def Error(page,err):
    callback = jsonify({f'{page}':f'{err}'})
    print(callback)
    return callback
  # def Reset():