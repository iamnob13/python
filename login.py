allowed_users = ['ariya-bk','gilda','mamad']
block_users = ['aliwch','cj','hamilton']
user = input ('username : ')
user = user.lower().strip() 
if user in block_users :
  print ('error, username blocked !')
elif user in allowed_users :
  print ('Login confirm')
else :
  print ('error, username wrong')