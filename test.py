# فایل تکست به هم ریخته را در قالب استاندارد جیسون ریخته و ذخیره کند
import json
my_list = []
try:
  with open('raw_data.txt','r') as file :
    for line in file :
      line = line.strip().split(',')
      name = line[0]
      count = int(line[1])
      balance = int(line[2])
      if count > 5 :
        status = 'available'
      else :
        status = 'low_stack'
      data ={
        'name':name,
        'count':count,
        'balance':balance,
        'status':status
      }
      my_list.append(data)
except FileNotFoundError:
  print('File Not Found Error')   
for i in my_list :
  print(i)
with open('cleaned_data.json','w') as file :
  json.dump(my_list,file,indent=4)



# raw data :
# Mobile,10,500
# Tablet,0,300
# Laptop,5,1000
# Charger,20,50