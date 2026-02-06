grocery = {
  'Apple':5,
  'Orange':3,
  'Lemon':7,
  'Banana':13,
  'Milk':0    
}
cart = {}



def get_answer(text) :
  answer = input(text)
  answer = answer.lower().strip()
  return answer


def see() :
  for name,number in grocery.items() :
    print(f'{name} : {number}')

def buy(text) :
  while True :
    name = input(text)
    name = name.title().strip()
    if name in grocery.keys() :
      if grocery[name] >= 1 :  
        grocery[name] = grocery[name] -1
        print('New list : ')
        see()
        if name in cart.keys():
          cart[name] = cart[name] + 1
        else :
          cart[name] = 1  
        return True
      else :
        print('Sold Out')
        return False
    else :
      print(f'We do not have "{name}"')
      return False
          

def sharj(text) :
  name = input(f'{text} /==> name : ')
  name = name.title().strip()
  while True :
    number = input(f'{text} /==> {name} number : ')
    try : 
      number = int(number)
      break
    except ValueError :
      print('Value Error')    
  if name in grocery.keys() :
    grocery[name] = grocery[name] + number
  else :
    grocery[name] = number
  print('New list : ')
  see()
  return True



while True :
  answer = get_answer('See /Buy /Sharj /Exit : ')
  if answer == 'see' :
    print('List : ')
    see()
    continue

  elif answer == 'buy' :
    total_buy = buy('Buy What : ')
    javab = input('Continue y/n : ')
    javab = javab.lower().strip()
    if javab == 'y' :
      continue
    elif javab == 'n' :
      break
    else :
      print('Wrong answer')
      continue  

  elif answer == 'sharj' :
    total_sharj = sharj('Name & number : ')
    javab = input('Continue y/n : ')
    javab = javab.lower().strip()
    if javab == 'y' :
      continue
    elif javab == 'n' :
      break
    else :
      print('Wrong answer')
      continue  

  elif answer == 'exit' :
    break

  else :
    print('Wrong answer')

print('Thank you')
print('Cart : ')
for name,number in cart.items() :
  print(f'{name} : {number}')
print('BYE')