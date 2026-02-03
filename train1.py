age = int(input ('please enter your age between 0 to 100 : '))
if age <=0 or age >=100 :
  print('wrong age')
elif age < 18 :
  print ('limited access')
elif 18<= age <60 :
  print ('welcome baby')
elif age >= 60 :
    print ('be careful Ezraiil right behind you')