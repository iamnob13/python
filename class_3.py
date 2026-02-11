class Student :
  def __init__(self,name,age,grade):
    self.name = name
    self.age = age
    self.grade = grade
  def is_honor_roll (self) :
    if self.grade > 18 :
      return True
    else :
      return False
    
class Classroom :
  def __init__(self,class_name):
    self.students = []
    self.class_name = class_name
  def add_students (self,student_obj) :
    self.students.append(student_obj)
  def show_all (self) :
    for i in self.students :
      print(f'{i.name}, Age : {i.age}, Grade : {i.grade} added to Math Class')
  def get_avg (self ) :
    total_sum = 0
    for i in self.students :
      total_sum += i.grade
    total_avg = total_sum / len(self.students)
    print(f'Math class average is ==> {total_avg}')
  def top_avg (self) :
    grade_list = []
    for i in self.students :
      grade_list.append(i.grade)
    if grade_list != [] :
      top = max(grade_list)
    else :
      print('No Student')
    for i in self.students :
      if top == i.grade :
        top_name = i.name
    print(f'Maximum average "===> {top_name}, Grade : {top}')

s1 = Student('Ariya',19,20)
s2 = Student('Gilda',20,19)
s3 = Student ('poriya',14,3)
my_students = [s1,s2,s3]

for i in my_students :
  print(i.name)
print('Grade > 18 : ')
for i in my_students :
  if i.is_honor_roll() :
    print(f'{i.name}, Grade ==> {i.grade}')

math_class = Classroom('Math')
math_class.add_students(s1)
math_class.add_students(s2)
print('Math class Students : ')
math_class.show_all()
math_class.get_avg()
math_class.top_avg()