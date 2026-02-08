# از بین تمام اطلاعات و لیست ها و دیکشنری ها نام و رشته ی کسانی که نمره بالاتر از 17 دارند را در یک فایل دیگر ذخیره کند
import json
try :
  with open('course.json','r') as file :
    data = json.load(file)
  
  my_list = []
  for first in data :
    for second in first['students'] :
      final_grade = (second['grade'])
      if final_grade > 17 :
        javab = (first['title'],second)
        my_list.append(javab)
  with open('top_score.json','w') as my_file :
    json.dump(my_list,my_file,indent=4)
  print('Done')
except FileNotFoundError:
  print('File Not Found Error')

# [
#   {
#     "course_id": 101,
#     "title": "Python Basics",
#     "students": [
#       {
#         "name": "Ali",
#         "grade": 18
#       },
#       {
#         "name": "Sara",
#         "grade": 15
#       }
#     ]
#   },
#   {
#     "course_id": 102,
#     "title": "Django Deep Dive",
#     "students": [
#       {
#         "name": "Reza",
#         "grade": 20
#       },
#       {
#         "name": "Mina",
#         "grade": 12
#       }
#     ]
#   }
# ]