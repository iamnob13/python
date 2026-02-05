laptop_stock = {
  'Acer':'100$',
  'Apple':'200$',
  'Lenovo':'50$',
  'Dell':'25$',
  'Hp':'15$',
  'Ommen':'35$',
  'Asus':'150$'
}
print('Laptop stock : ')
for model,price in laptop_stock.items() :
  print(f'{model} : {price}')
print('End')  
model = input('Model : ')
model = model.title().strip()
price = laptop_stock.get(model,'Mojood nist')
print(f'{model} : {price}')