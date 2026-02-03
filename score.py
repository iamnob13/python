score_list = []
for i in range(3) :
  name = input('Please enter your "name" : ')
  score = input(f'Please enter {name} "score" : ')
  try :
    score = int(score)
    score_list.append(score)
  except :
    print('Error, Please enter the correct score : ')
    continue
total_sum = sum(score_list)
avg = sum(score_list)/len(score_list)
print('Total sum : ',total_sum)
print('Score average : ',avg)