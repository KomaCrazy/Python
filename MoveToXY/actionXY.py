import math

set_x = 2
set_y = 2

target_x = 4
target_y = 4

set_xy = [set_x,set_y]
target_xy = [target_y,target_x]

def coordianates(set1,set2 : list) -> int :
  return math.sqrt((abs(set1[0] - set2[0])**2) + (abs(set1[1] - set2[1])**2))

print(coordianates(target_xy,set_xy))
