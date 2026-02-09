# شروع یاد گیری کلس و اپجکت و برنامه نویسی شی گرا | تمرینات ساده برای یادگیری 
# کلس قهرمانان | اسم و اچ پی رو میگیره | و یک تارگت انتخاب میکنه در نهایت 
class Hero :
  def __init__(self,name,health):
    self.name = name
    self.health = health

  def introduce (self) :
    print(f'I am {self.name} with {self.health} HP')

  def attack(self,target) :
    if target.health <= 0 :
      print(f'{target.name} already lost')
      return
    target.health -= 10
    print(f'{self.name} attacked to {target.name}')
    if target.health < 0 :
      target.health = 0

h1 = Hero('Ariya',100)
h2 = Hero('Gilda',93)
h3 = Hero('Poriya',9)
my_hero = [h1,h2,h3]

final_target = None
my_target = input('Target : ').title().strip()
for i in my_hero :
  if not h1.name == my_target :
    if i.name == my_target :
      final_target = i
      if final_target :
        h1.attack(final_target)
      else :
        print('Target Not Founded')
      break
  else :
    print('You can not attack yourself')
    break    

for i in my_hero :
  i.introduce()