allowed_users = ['ariya-bk','gilda','mamad']
user = input ('enter your username to login : ')
user = user.lower().strip() #متد  ها واسه یوزر نیم
if user in allowed_users :
  print ('OK, welcome back my love')
else :
  print ('Your username was wrong,Please try again')  
