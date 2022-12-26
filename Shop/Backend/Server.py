from Tools.Tools import *



@app.route("/")
async def PageMain():
 try:
   return '0'
 except Exception as e :
   return Server.Error("PageMain",e)

@app.route("/find")
async def PageFind():
 try:
   await Sql(Manage(request.args))
   return '0'
 except Exception as e :
   return Server.Error("PageFind",e)
    
    
    
if '__main__' == __name__:
  Server.Run()
