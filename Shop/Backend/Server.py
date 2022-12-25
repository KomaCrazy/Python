from Fuc.Tools import *

@app.route('/')
def PageMain():
  return '0'

@app.route('/create_db')
def PageCreateDB():
 try:
  debug = Sql(request.args).Create()
  return jsonify(debug)
 except Exception as e :
  return jsonify({"Route Error":"PageCreateDB"})
 
@app.route('/add_user')
def PageAdd():
  debug = Sql(request.args).Find()
  return '0'


if __name__ == '__main__':
  Server.Run()
