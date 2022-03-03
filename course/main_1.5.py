age = "18"
print(type(age))
n_age = int(age)
print(n_age)
print(type(n_age))

#who-positional인자(arguments)#
def say_hello(who): 
  print("hello",who)
  print("bye")
#안에 들여써야 함수로 포함 됨.#

say_hello("Nicolas")
#인자(who)를 받아("nicolas")줘야 에러 안뜸#

def plus(a,b):
  print(a+b)

def minus(a,b=0):
  print(a-b)

#b=0 defalt value. b자리에 인자 안넣어도 0으로 자동계산.
plus(2,5)
minus(2)

def say_hi(name="anonymous"):
  print("hello",name)

say_hi()
say_hi("mangji")

