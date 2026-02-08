import json

zero = []
total_sum = 0
try:
  with open('inventory.json','r') as file :
    data = json.load(file)
  for i in data :
    if i['category'] == "electronics" :
      i['price'] = i['price']*0.1 + i['price']
    total_sum = total_sum + i['price'] * i['count'] 
    count = i['count']
    if count == 0 :
      zero.append(i['name'])
  print('zero count : ')
  print(zero)
  print('Balance : ')
  print(total_sum)
  with open('inventory.json','w') as my_file :
    json.dump(data,my_file,indent=4)
  print('Update done')
except FileNotFoundError:
  print('File Not Found Error')


# [
#     {
#         "id": 1,
#         "name": "Laptop",
#         "price": 1320.0,
#         "count": 5,
#         "category": "electronics"
#     },
#     {
#         "id": 2,
#         "name": "Mouse",
#         "price": 27.5,
#         "count": 0,
#         "category": "electronics"
#     },
#     {
#         "id": 3,
#         "name": "Keyboard",
#         "price": 88.0,
#         "count": 10,
#         "category": "electronics"
#     },
#     {
#         "id": 4,
#         "name": "Bread",
#         "price": 2,
#         "count": 50,
#         "category": "food"
#     }
# ]