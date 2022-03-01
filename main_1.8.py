def r_plus(a,b):
  return a+b
  print("sometihnfaj;f",True)

def p_plus(a,b):
  print(a+b)


p_result = p_plus(2,3)
r_result = r_plus(2,4)

print(r_result)
#return 하고나면 함수는 종료된다. print 출력안됨.

def minus(a,b):
  return a - b

#keyword argument 위치가 아닌 이름으로 인자 매칭
result = minus(b=30, a=1)
print(result)

def say_hello(name, age):
  return f"hello {name} you are {age} years old"
#or return "hello" + name + "you are" + age + " years old"

hello = say_hello(name="nico", age="12")
print(hello)