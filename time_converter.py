# convert to ( minute : second )
def convert(text):
  while True :
    time = input(text)
    try :
      time = int(time)
      return (f'{time//60}:{time%60}')
    except ValueError:
      print('Value Error')
final_convert = convert('Enter time : ')  
print('minute:second')
print(final_convert)