class Func1 :
  def __init__(self,data) -> None:
    self.box1 = data 

class Func2(Func1) :
  def __init__(self) -> None:
    self.db = self.box1


func1 = Func1("kaw")
func2 = Func2()
print(func1.box1)
print(func2.db)