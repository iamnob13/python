my_archive = {
  ######### Genres should bi in list & Rating should be integer چون مثلا فیلمای بالاتر از 9 
  'Breaking_bad' : {'Title':'Breaking bad','Year':2008,'Genres':['Drama'],'Rating':9.5,'Is_series':True},
  'Inception' : {'Title':'Inception','Year':2010,'Genres':['Sci_fi','Action'],'Rating':8.8,'Is_series':False},
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

print('==========')
print('Action : ')
for i in my_archive.keys() :
  genre = my_archive[i]['Genres']
  if 'Action' in genre :
    print(i)
print('==========')