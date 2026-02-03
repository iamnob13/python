block_users = ['aliwch','cj','hamilton']
user = input('enter your username : ')
user = user.lower().strip()
if user in block_users :
  print ('Your username is blocked !')
else :
  print ('All fine')  