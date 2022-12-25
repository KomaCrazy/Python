import sqlite3


  
def Sql2Json():
  path = sqlite3.connect("./db.db")
  table = []
  found_data = path.execute(f'select * from std;')
  found_topic = path.execute(f'pragma table_info(std)')
  Lists = []
  
  for i in found_data :
    data = {"id":i[0],"user":i[1]}
    print(data)
    
Sql2Json()