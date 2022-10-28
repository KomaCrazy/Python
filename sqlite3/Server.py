from xml.dom.minidom import Document
from tools import * 


@app.route("/")
def about():
  return jsonify(TEXT.Document())

@app.route("/robot_add")
def robot_add():
  return jsonify(Sql.add(request.args))

SERVER.Run()