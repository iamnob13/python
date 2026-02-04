def safe_num(text) :
  while True :
    number = input(text)
    number = number.strip()
    try :
      number = int(number)
      return number
    except ValueError :
      print('Value Error')