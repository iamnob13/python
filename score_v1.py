# this code get  3 name and 3 score 
# tell you if some one Failed
def get_score(text) :
  while True :
    score = input(text)
    try :
      score = float(score)
      if 0<= score <=20 :
        return score
      else :
        print('value error')
    except ValueError:
      print('value error')
def get_name(text) :
  while True :
    name = input(text)
    name = name.strip()
    if len(name) == 0 :
      print('Name error')
    else :  
      name = name.title()
      return name
all_name =[]
all_score =[]
for i in range(3) :
  all_name.append(get_name('Name : '))
  all_score.append(get_score('Score : '))
for i in range(len(all_score)) :
  name = all_name[i]
  score = all_score[i]
  if score < 10 :
    print(f'{name} Failed')
  else :
    print(f'{name} Passed')