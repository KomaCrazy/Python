from Fuc.Tools import *

@app.route('/')
def PageMain():
  return '0'

@app.route('/create_db')
def PageCreateDB():
  sql = Sql(request.args)
  sql.Create()
  return 'ok'

if __name__ == '__main__':
  Server.Run()
