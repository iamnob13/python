import json


class Product :
  def __init__(self,name,price,stock):
    self.name = name
    self.price = price
    self.stock = stock

  def is_available (self) :
    if self.stock > 0 :
      return True
    else :
      return False
  def get_total_value (self) :
    javab = self.price * self.stock
    return javab 



class Fased(Product) :
  def __init__(self, name, price, stock,expired_date):
    super().__init__(name, price, stock)
    self.expired_date = expired_date
  def show (self) :
    print(f'{self.name} value ===> {self.get_total_value()}')
    print(f'{self.name} Expired date ===> {self.expired_date}')
  def is_available (self) :
    if self.expired_date > '2026-05-10' :
      return False
    else :
      if self.stock > 0 :
        return True
      else :
        print('Mojood nist')


class Warehouse :
  def __init__(self,warehouse_name):
    self.my_list = []
    self.warehouse_name = warehouse_name
  def add_product(self,product) :
    self.my_list.append(product)
    return self.my_list
  def find_expensive (self) :
    expensive = []
    top_expensive = []
    for i in self.my_list :
      expensive.append(i.price)
    if expensive != [] :
      max_list = max(expensive)
      for i in self.my_list :
        if i.price == max_list:
          top_expensive.append(i.name)
      return top_expensive
    else :
      print('Kala Nist')
      return False
  def inventory_report (self) :
    print(f'{self.warehouse_name} Product List : ')
    for i in self.my_list :
      print(i.name)
    print('================')
    count = 0
    for i in self.my_list :
      javab = i.price * i.stock
      count += javab
    return count
  
  def transfer_to (self,product,warehouse_target) :
    found = None
    for i in self.my_list :
      if i.name == product :
        found = i
        break
    if found :
      self.my_list.remove(found)
      warehouse_target.add_product(found)
      print('Transferred ok')
    else :
      print('Kala nist')
try:
  with open('my_product.json','r') as file :
    my_file = json.load(file)
  my_data = []
  for i in my_file :
    if 'expired_date' in i :
      obj = Fased(i['name'],i['price'],i['stock'],i['expired_date'])
      my_data.append(obj)
    else : 
      obj = Product(i['name'],i['price'],i['stock'])
      my_data.append(obj)
except FileNotFoundError :
  print('File Not Found Error')

p1 = Product('apple',3,33)
p2 = Product('phone',100,25)
p3 = Product('shoes',10,50)
p4 = Product('banana',2,78)
p5 = Fased('milk',1,100,'2026-05-11')
p6 = Product('laptop',200,0)
my_list = [p1,p2,p3,p4,p5,p6]
if p6.is_available() :
  print(f'{p6.name} is available')
else : 
  print(f'{p6.name} is unavailable')

print(f'Total value of {p2.name} : {p2.get_total_value()}')
ariya_warehouse = Warehouse('Ariya')
gilda_warehouse = Warehouse('Gilda')
mamad_warehouse = Warehouse('Mamad')
ariya_warehouse.add_product(p2)
ariya_warehouse.add_product(p3)
ariya_warehouse.add_product(p6)
gilda_warehouse.add_product(p1)
gilda_warehouse.add_product(p5)
mamad_warehouse.add_product(p4)
print(f'Most Expensive  Product ==> {ariya_warehouse.find_expensive()}')
ariya_warehouse.transfer_to('phone',gilda_warehouse)
print(f'All Gilda balance ==> {gilda_warehouse.inventory_report()}')
p5.show()
javab = p5.is_available()
if javab :
  print(f'{p5.name} is available')
else :
  print(f'{p5.name} Expired')

finally_list = []
for j in my_list :
  my_product = {
    'name':j.name,
    'price':j.price,
    'stock':j.stock
  }
  if hasattr(j,'expired_date') :
    my_product['expired_date'] = j.expired_date
  finally_list.append(my_product)
with open('my_product.json','w') as file :
  json.dump(finally_list,file,indent=4)

