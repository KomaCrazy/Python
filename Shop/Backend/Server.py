from Fuc.Tools import *

@app.route('/')
def PageMain():
  return '0'

@app.route('/create_db')
def PageCreateDB():
  Manage(request.args)
  Sql.Create()
  return 'ok'

if __name__ == '__main__':
  Server.Run()
