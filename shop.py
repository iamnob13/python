fruit1 = input ('write fruit 1 : ')
fruit1 = fruit1.lower().strip()
fruit2 = input ('write fruit 2 : ')
fruit2 = fruit2.lower().strip()
fruit3 = input ('write fruit 3 : ')
fruit3 = fruit3.lower().strip()
fruit4 = input ('write fruit 4 : ')
fruit4 = fruit4.lower().strip()
fruit5 = input ('write fruit 5 : ')
fruit5 = fruit5.lower().strip()
fruits = [fruit1,fruit2,fruit3,fruit4,fruit5]
for my in fruits :
  if my == 'apple':
    print ('Your list is : ',my,'.but apple has sold out')
  else:  
   print ('Your list is : ',my)