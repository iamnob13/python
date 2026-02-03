items = []
while True :
    price = input ('Please enter price of your item, enter "Done" when finished : ')
    price = price.lower().strip()
    if price == 'done' :
      break
    else :
      try :
        price = float(price)
        items.append(price)
      except ValueError:
        price = input ('error, please enter the number : ')
        continue  
total_sum = sum(items)
print ('your sum of your price is : ',total_sum,'$')