import os
os.system('clear')


class DemoPlainClass:
    a: int           # <1>
    b: float = 1.1   # <2>
    c = 'spam'       # <3>


print(DemoPlainClass.__annotations__)
print(DemoPlainClass.b)
print(DemoPlainClass.c)
# print(DemoPlainClass.a)

o = DemoPlainClass()
print(o.__class__.__dict__)
