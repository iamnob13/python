import psycopg2
import os 
from dotenv import load_dotenv

class Students_db :
  def __init__(self):
    self.connection = None
    try :
      load_dotenv()
      user = os.getenv('DB_USER')
      password = os.getenv('DB_PASSWORD')
      self.connection = psycopg2.connect (
        user = user,
        password = password,
        host = '127.0.0.1',
        port = '5432',
        database = 'postgres'
      )
      self.cursor = self.connection.cursor()
    except Exception as e :
      print(f'connection fail {e} ')

  def get_all_students (self) :
    if self.connection :
      self.cursor.execute('SELECT first_name,last_name FROM students')
      show = self.cursor.fetchall()
      return show 
    else :
      print('Database not founded')
      return []

  def add_student (self,first_name,last_name,score) :
    if self.connection :
      new_student = (first_name,last_name,score)
      query = 'INSERT INTO students (first_name,last_name,score) VALUES (%s,%s,%s)'
      self.cursor.execute(query,new_student)
      self.connection.commit()
    else :
      print('Database not founded')
      return False

  def update_student_score (self,id,score):
    if self.connection :
      data = (score,id)
      query = 'UPDATE students SET score = %s WHERE id = %s'
      self.cursor.execute(query,data)
      self.connection.commit()
    else :
      print('Database not founded')
      return False
    
  def delete_student (self,id) :
    if self.connection :
      data = id,
      query = 'DELETE FROM students WHERE id = %s'
      self.cursor.execute(query,data)
      self.connection.commit()
    else :
      print('Database not founded')
      return False

  def close (self) :
    if self.connection :
      self.cursor.close()
      self.connection.close()
      print('Connection End')
    else :
      print('Database not founded')
      return []

db = Students_db()

while True:
    print("\n" + "="*20)
    print("1. Show All Students")
    print("2. Add New Student")
    print("3. Update Score")
    print("4. Delete Student")
    print("5. Exit")
    print("="*20)
    
    choice = input("Choose an option: ").strip()

    if choice == '1':
        students = db.get_all_students()
        print("\n--- Student List ---")
        for s in students:
            print(f"Name: {s[0]} {s[1]}")

    elif choice == '2':
        fn = input("First Name: ")
        ln = input("Last Name: ")
        sc = float(input("Score: "))
        db.add_student(fn, ln, sc)
        print("Student added!")

    elif choice == '3':
        sid = int(input("Student ID: "))
        nsc = float(input("New Score: "))
        db.update_student_score(sid, nsc)
        print("Score updated!")

    elif choice == '4':
        sid = int(input("Student ID to delete: "))
        db.delete_student(sid)
        print("Student deleted!")

    elif choice == '5':
        db.close()
        break

    else:
        print("Invalid choice!")