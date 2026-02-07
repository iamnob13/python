# یه پروژه واسه تمرین دیکشنری ها | مدیریت پول و کیف پول | try /except | function 
user = {
  'Ariya': {'Age':18,'Balance':500},
  'Gilda': {'Age':20,'Balance':100},
  'Mamad': {'Age':13,'Balance':0}
}
#print (user.get('Ariya','none')['Age'])

def deposit (name,amount):
  if name in user.keys() :
    while True :
      try :
        amount = float(amount)
        user[name]['Balance'] += amount
        print(f'{name} ==> Balance : {user[name]['Balance']}')
        return True
      except ValueError:
        print('Value Error')  
  else:
    print('User not found')  
    return False


def transfer(tra,rec,amount) :
  if tra in user.keys() :
    while True:
      try :
        amount = float(amount)
        mojodi = user[tra]['Balance']
        if mojodi >= amount :
          user[tra]['Balance'] = user[tra]['Balance'] - amount

          if rec in user.keys() :
            user[rec]['Balance'] += amount
            return True
          else :
            user[rec] = {'Age':0,'Balance':amount}  
            return True
        else :
          print('Not enough balance')
          return False   
      except ValueError:
        print('Value Error')  
  else :
    print('User not found')
    return False 


name = input('Name :' )
name = name.title().strip()
amount = input('Amount : ')
javab = deposit(name,amount)
if javab :
  print('Deposit successful')
else :
  print('Deposit failed')


tra = input('Sender : ')  
tra = tra.title().strip()
rec = input('Receiver : ')
rec = rec.title().strip()
amount = input('Amount : ')
javab = transfer(tra,rec,amount)
if javab :
  print('Transfer successful')
else :
  print('Transfer failed')
for key,value in user.items() :
  print(key,value)
