class Product:
  def __init__(self,name,price) :
    self.name = name
    self.price = price
    pass


class Cart :
  def __init__(self):
    self.items = []
  def add_product(self,opj) :
    self.items.append(opj)
  def total_price(self) :
    total_sum = 0
    for i in self.items :
      total_sum += i.price
    return total_sum
  # def show_cart(self) :
  #   for i in self.items :
  #     print(i.name)


p1 = Product('Laptop',200)
p2 = Product('Milk',10)
p3 = Product('Phone',100)
my_product = [p1,p2,p3]
my_cart = Cart()
print('The List : ')
for i in my_product :
  print(i.name)



ghat = False
while True :
  buy = input('Buy What /or finish : ').title().strip()
  if buy == 'Finish' :
    ghat = True
    break
  else :
    javab = False
    for i in my_product :
      if i.name == buy :
        my_cart.add_product(i)
        print(f'{i.name} added to cart')
        javab = True
# print(my_cart.show_cart())


if javab == True:    
  print(f'Total price is {my_cart.total_price()}$')
if ghat == True :
  print('bye')