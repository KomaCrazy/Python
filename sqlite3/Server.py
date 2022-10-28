from pprint import pprint
from xml.dom.minidom import Document
from tools import * 


@app.route("/")
def about():
  return jsonify(TEXT.Document())

@app.route("/robot_add")
def robot_add():
 try:
  return jsonify(Sql.add(request.args))
 except Exception as e:
  return {"status":"Add Robot Fail"}

@app.route("/robot_delete")
def robot_delete():
 try:
  return jsonify(Sql.delete(request.args))
 except Exception as e:
  print(e)
  return {"status":"delete Robot Fail"}

@app.route("/robot_show")
def robot_show():
 try:
  return jsonify(Sql.show(request.args))
 except Exception as e:
  print(e)
  return {"status":"show Robot Fail"}

@app.route("/robot_edit")
def robot_edit():
 try:
  return jsonify(Sql.edit(request.args))
 except Exception as e:
  print(e)
  return {"status":"Edit Robot Fail"}

SERVER.Run()