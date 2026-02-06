grocery = {
  'Apple': {'count':5,'price':1},
  'Orange': {'count':3,'price':2},
  'Lemon': {'count':7,'price':4},
  'Banana': {'count':13,'price':8},
  'Milk': {'count':0,'price':10}
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
      if grocery[name]['count'] >= 1 :  
        grocery[name]['count'] = grocery[name]['count'] -1
        print('New list : ')
        see()
        if name in cart.keys():
          cart[name]['count'] = cart[name]['count'] + 1
          cart[name]['price'] = cart[name]['price'] + grocery[name]['price']
        else :
          cart[name] = {'count':1 , 'price': grocery[name]['price']}
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
    grocery[name]['count'] = grocery[name]['count'] + number
  else :
    while True :
      gheymat = input('Price : ')
      try :
        gheymat = int(gheymat)
        break
      except ValueError:
        print('Value error')  
    grocery[name] = {'count':number , 'price':gheymat}  
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
      #break
      pass
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

print('=====================')
print('Thank you')
print('Cart : ')
for name,number in cart.items() :
  print(f"{name} : {number}$")
print('BYE')
print('=====================')