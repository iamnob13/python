score_list = []
for i in range(3) :
  name = input('"name" : ')
  while True :    # وایل یه لوپ میسازه که مجبورش کنه
    score = input(f'"Score" for {name} : ')
    score = score.strip()
    try :
      score = float(score)
      score_list.append(score)
      break
    except ValueError:
      print('Error, Please enter the correct score : ')
total_sum = sum(score_list)
avg = sum(score_list)/len(score_list)
print('Total sum : ',total_sum)
print('Score average : ',avg)