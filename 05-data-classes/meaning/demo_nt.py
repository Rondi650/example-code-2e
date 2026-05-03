import typing

class DemoNTClass(typing.NamedTuple):
    a: int           # <1>
    b: float = 1.1   # <2>
    c = 'spam'       # <3>


print(DemoNTClass.__annotations__)
print(DemoNTClass.a)
print(DemoNTClass.b)
print(DemoNTClass.c)

print(DemoNTClass.__doc__)


nt = DemoNTClass(8)
print(nt)
print(nt.c)

nt.a = 5
nt.z = 5