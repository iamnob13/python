my_archive = {
  ######### Genres should bi in list & Rating should be integer چون مثلا فیلمای بالاتر از 9 
  'Breaking_bad' : {'Title':'Breaking bad','Year':2008,'Genres':['Drama'],'Rating':9.5,'Is_series':True},
  'Inception' : {'Title':'Inception','Year':2010,'Genres':['Sci_Fi','Action'],'Rating':8.8,'Is_series':False},
  'Whiplash' : {'Title':'Whiplash','Year':2014,'Genres':['Drama','Indie'],'Rating':8.5,'Is_series':False}
}
#========NOTHING==================#
#print(my_archive['Whiplash']['Year'])
#print(my_archive['Whiplash']['Genres'][0])
#my_archive['Breaking_bad']['Is_series'] = False
#print(my_archive['Breaking_bad']['Is_series'])
#========NOTHING==================#

print('==========')
for i in my_archive.keys() :
  imdb = my_archive[i]['Rating']
  if imdb >= 8.6 :
    print(f'{i} IMDB ===> {imdb}')


print('==========')
print('Movies : ')

for i in my_archive.keys() :
  movie = my_archive[i]['Is_series']
  if movie ==False :
    print(i)


def get_genre (answer) :
  answer = answer.title().strip()
  return answer
count = 0
print('==========')
print('user genre : ')
answer = input('Choose genre : ')
user_genre = get_genre(answer)
for key,value in my_archive.items() :
  if user_genre in value['Genres'] :
    print(key)
    count += 1
if count == 0 :
  print('None') 
print('==========')