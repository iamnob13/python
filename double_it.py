def get_number(num) :
  while True :
    number = input(num)
    try :
      number = float(number)
      return number
    except ValueError:
      print('value error')  
def double_it (a) :
  double = a * 2
  return double
number = get_number('Number : ')
number = double_it(number)
print(f'Double it ==> {number}')