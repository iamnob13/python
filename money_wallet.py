# یه پروژه واسه تمرین دیکشنری ها | مدیریت پول و کیف پول | try /except | function | اطلاعات روی فایل ذخیره میشود با هربار تغییر در موجودی | just training json.
import json

user = {
  'Ariya': {'Age':18,'Balance':500},
  'Gilda': {'Age':20,'Balance':100},
  'Mamad': {'Age':13,'Balance':0}
}

def save () :
  with open('Bank.json','w') as my_file :
    json.dump(user,my_file,indent=4)
    return True
try:
  with open('Bank.json','r') as file :
    user = json.load(file)
except FileNotFoundError :
  save()

def log (a) :
  with open('log.txt','a') as log :
    log.write(a + '\n')

def deposit (name,amount):
  if name in user.keys() :
    while True :
      try :
        amount = float(amount)
        user[name]['Balance'] += amount
        print(f'{name} ==> Balance : {user[name]['Balance']}')
        a = f'{name} deposited {amount}$'
        log(a)
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
          if rec in user.keys() :
            user[tra]['Balance'] = user[tra]['Balance'] - amount
            user[rec]['Balance'] += amount
            a = f'{tra} transferred {amount}$ to {rec}'
            log(a)
            return True
          else :
            final = con(rec)
            if final :
              user[rec] = {'Age':0,'Balance':amount}  
              log(a)
              return True
            else :
              return False
        else :
          print('Not enough balance')
          return False   
      except ValueError:
        print('Value Error')  
  else :
    print('User not found')
    return False 
def con(text) :
  while True :
    con = input(f'{text} y/n : ')
    con = con.lower().strip()
    if con == 'y' :
      return True
    elif con == 'n' :
      return False
    
#def show_history () :
  with open('log.txt','r') as show :
    json.load(show)
    show.write(show)
    history = show.write()
    return history




final_con = con('Deposit')  
if final_con :
  name = input('Name :' )
  name = name.title().strip()
  amount = input('Amount : ')
  javab = deposit(name,amount)
  if javab :
    print('Deposit successful')
    save()
  else :
    print('Deposit failed')

final_con = con('Transfer')
if final_con :
  tra = input('Sender : ')  
  tra = tra.title().strip()
  rec = input('Receiver : ')
  rec = rec.title().strip()
  amount = input('Amount : ')
  javab = transfer(tra,rec,amount)
  if javab :
    print('Transfer successful')
    save()
  else :
    print('Transfer failed')
print('===================')
for key,value in user.items() :
  print(f'{key},{value}$')
print('===================finished')
