import random
while True :
  low = input('Lowest : ')
  low = low.strip()
  try:
    low = int(low)
    break
  except ValueError:
    print('Value Error')
while True :  
  high = input('Highest : ')
  high = high.strip()
  try:
    high = int(high)
    break
  except ValueError:
    print('Value Error')
if low > high :
  print('Value Error')
else :
  count = 0
  while True :
    if low > high :
      break
    else :
      try :
        guess = random.randint(low,high)  
        count = count + 1
        print('My guess : ',guess)
        answer = input('Kamtar/ Bishtar/ Dorost/ ? ')
        answer = answer.lower().strip()
        if answer == 'dorost' :
          print('yeahhh, Right')
          break
        elif answer == 'kamtar' :
          high = guess -1
        elif answer == 'bishtar' :
          low = guess + 1
        else :
          print('Error')  
      except ValueError:
        print('Value Error')
  if low>high :      
    print('Value Error')
  else :  
    print('Total guess : ',count)
    print('Answer : ',guess)  