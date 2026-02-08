import json

block_users = ['Aliwch','Cj','Hamilton']

def save() :
  with open('blacklist.json','w') as file:
    json.dump(block_users,file,indent=5)

def read():
  try :
    with open('blacklist.json','r') as file :
      data = json.load(file)
      return data
  except FileNotFoundError:
    save()
    return block_users    

def con(name) :
  while True :
    answer = input(f'Add {name} to block list y/n : ')
    answer = answer.lower().strip()
    if answer == 'y' :
      return True
    elif answer == 'n' :
      return False

block_users = read()


name = input('User name : ')
name = name.title().strip()
if name in block_users :
  print('Access Denied')
else :
  if con(name) :
    block_users.append(name)
    print('================')
    print('New list : ')
    print(block_users)
    save()
  else :
    print('Bye')
