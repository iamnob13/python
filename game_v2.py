# همون بازی ورژن یک هست فقط ایندفعه شما باید عدد رندوم سیستم رو حدس بزنید
import random
def safe_num(text) :
  while True :
    number = input(text)
    number = number.strip()
    try :
      number = int(number)
      return number
    except ValueError :
      print('Value Error')
low = safe_num('Lowest : ')
high = safe_num('Highest : ')
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
