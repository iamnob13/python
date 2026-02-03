age = int(input ('please enter your age between 0 to 100 : '))
if age <=0 or age >=100 :
  print('wrong age')
else:  
  if age < 18 :
    print ('limited access')
  if age >= 18 and age < 60:
    print ('welcome baby')
  if age >= 60 :
    print ('be careful you are too old')
