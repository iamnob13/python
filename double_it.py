def double_it (a) :
  double = a * 2
  return double 
while True :
  number = input('Number : ')
  try :
    number = float(number)
    break
  except ValueError:
    print('value error')
javab = double_it(number)
print(javab)