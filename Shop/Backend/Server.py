from Fuc.Tools import *

@app.route('/')
def PageMain():
  return '0'

@app.route('/create_db')
def PageCreateDB():
  x = (Manage(request.args))
  print(x.db_name)
  print(x.db_target)
  
  return 'ok'

if __name__ == '__main__':
  Server.Run()
