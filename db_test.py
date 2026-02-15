import psycopg2
# first_name = input('First Name : ').lower().strip()
# last_name = input('Last Name : ').lower().strip()
# while True :
#   score = input('Score : ').strip()
#   try:
#     score = int(score)
#     break
#   except ValueError :
#     print('Value Error') 
try :
  connection = psycopg2.connect(
    user = 'postgres',
    password = '13313',
    host = '127.0.0.1',
    port = '5432',
    database = 'postgres'
  )
  cursor = connection.cursor()

  # new_student = (first_name,last_name,score)
  # query ='INSERT INTO students (first_name,last_name,score) VALUES (%s,%s,%s)'
  # cursor.execute(query,new_student)
  # connection.commit()


  cursor.execute('SELECT * FROM students')
  javab = cursor.fetchall()
  print("-" * 50)
  print("ID | First Name | Last Name | Score")
  print("-" * 50)
  for row in javab: 
    print(f"{row[0]}  | {row[1]:<10} | {row[2]:<10} | {row[4]}")
  print("-" * 50)

  # target_id = input('Target ID /enter for no : ').strip()
  # if target_id :
  #   try :
  #     cursor.execute('DELETE FROM students WHERE id = %s ',(target_id,))
  #     connection.commit()
  #     print(f'ID {target_id} DELETED')
  #   except :
  #     print('ID not founded')


except Exception as e :
  print(f'Error{e}')
finally :
  if connection :
    cursor.close()
    connection.close()
    print('END')