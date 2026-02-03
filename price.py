price = input ('Please enter price of your item : ')
price = price.strip()
try :
  price = float(price)
except :
  price = input ('error, plese enter the number : ')  
print ('your price is : ',price,'$')