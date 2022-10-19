import math

class Point :
  def __init__(self,data) -> None :
    self.x = data["x"]
    self.y = data["y"]
  def __int__(self) -> int :
    return self.x
  def __int__(self) -> int :
    return self.y

def way(set,target:list):
  print(set,target)