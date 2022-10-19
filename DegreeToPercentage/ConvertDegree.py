import math
def PrecenToDegress(data: int) -> int :
  deg = data['deg']
  cur = data['cur']
  return math.trunc(cur * 100 / deg)

deg = 360
cur = 180
data = {"deg":deg,"cur":cur}

print(PrecenToDegress(data),"%")