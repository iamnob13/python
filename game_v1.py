#یه بازی کوچیک که سیستم عدد ذهنیتون رو با راهنمایی پیدا میکنه
import random
answer = random.randint(1,100)
count = 0
while True :
  user_num = input('guess answer : ')
  user_num = user_num.strip()
  try :
    user_num = int(user_num)
    count = count + 1
    if user_num == answer :
      print('yeahhhh, Right')
      break
    elif user_num > answer :
      print('Kamtar')
    elif user_num < answer :
      print('Bishtar')  
  except ValueError:
    print('choose " number "')
print('Total guess : ',count)
print('answer : ',answer)
