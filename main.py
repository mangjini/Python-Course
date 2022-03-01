days = ("Mon","Tue", "Wed","Thu", "Fri")

for day in days : 
  if day == "Wed":
    break
  else:
    print(day)

for letter in "mangji":
  print(letter)


#module import(모듈전체, 사용하지않는것도)
import math

#모듈 중 필요한 것만 import
from math import ceil, fsum as cool_sum
#fsum에 이름 붙여줌 (cool_sum)

print(math.ceil(1.2))
print(cool_sum([1,2,3,4,5]))


from calculator import plus,minus

print(plus(1,2),minus(1,2),True,"llalalala",True,"fkdkfslfslf")