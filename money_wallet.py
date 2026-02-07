user = {
  'Ariya': {'Age':18,'Balance':500},
  'Gilda': {'Age':20,'Balance':100},
  'Mamad': {'Age':13,'Balance':0}
}
#print (user.get('Ariya','none')['Age'])

def deposit (text):
  name = input(text)
  name = name.title().strip()
  if name in user.keys() :
    while True :
      amount = input('Amount : ')
      try :
        amount = float(amount)
        user[name]['Balance'] += amount
        print(f'{name} ==> Balance : {user.get(name)['Balance']}')
        return True
      except ValueError:
        print('Value Error')  
  else:
    print('User not found')  
    return False


def transfer(text) :
  tra = input(text)
  tra = tra.title().strip()
  if tra in user.keys() :
    rec = input('Receiver : ')
    rec = rec.title().strip()
    while True:
      amount = input('Amount : ')
      try :
        amount = float(amount)
        mojodi = user[tra]['Balance']
        if mojodi >= amount :
          user[tra]['Balance'] = user[tra]['Balance'] - amount

          if rec in user.keys() :
            user[rec]['Balance'] += amount
            return True
          else :
            user[rec] = {'Balance':amount}  
            return True
        else :
          print('Not enough balance')
          return False   
      except ValueError:
        print('Value Error')  
  else :
    print('User not found')
    return False 



javab = deposit('Name : ')
if javab :
  print('Deposit successful')
else :
  print('Deposit failed')

javab = transfer('Sender : ')
if javab :
  print('Transfer successful')
else :
  print('Transfer failed')
for key,value in user.items() :
  print(key,value)