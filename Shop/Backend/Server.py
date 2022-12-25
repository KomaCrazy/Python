from Tools.Tools import *



@app.route("/")
def PageMain():
 try:
  return '0'
 except Exception as e :
   return Server.Error("PageMain",e)

@app.route("/find")
def PageFind():
 try:
   print("<Here")
   Manage(request.args)
   return '0'
 except Exception as e :
   return Server.Error("PageFind",e)
   
if '__main__' == __name__:
  Server.Run()
