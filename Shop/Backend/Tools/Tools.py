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
    print(self.table)
    print(self.field)
        
        



class Server :
  def Run():
      app.run('0.0.0.0',5000)
  
  def StatusOK(page):
    return jsonify({f'{page}':f'OK'})
  
  def Error(page,err):
    return jsonify({f'{page}':f'{err}'})  
  # def Reset():