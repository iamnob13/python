numbers = []
while True:
  user_num = input('Enter number, Enter " -1 " to see average : ')
  user_num = user_num.strip()
  try :
    user_num = float(user_num)
    if user_num == -1 :
      break
    else:
      numbers.append(user_num)
  except ValueError:
    print('Error, Wrong data')
if numbers == []:
  print('Zero number')
else:      
  total_avg = sum(numbers)/len(numbers)
  print('Average : ',total_avg)