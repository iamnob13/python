allowed_users = ['ariya-bk','gilda','mamad']
block_users = ['aliwch','cj','hamilton']
user = input ('enter your username to login : ')
user = user.lower().strip()
if user in block_users :
  print ('error, Your username is blocked !')
elif user in allowed_users :
  print ('fine, welcome back my love')
else :
  print ('error, Your username was wrong,Please try again')