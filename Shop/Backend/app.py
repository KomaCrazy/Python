target = ["id","name","age"]
table = "db"
def create(table,target):
  cmd = f'select'
  for i in target :
    if i == target[len(target)-1] :
     cmd = cmd + f',{i} from {table};'
    else : 
      cmd = cmd + f' {i},'
  return cmd

print(create(table,target))