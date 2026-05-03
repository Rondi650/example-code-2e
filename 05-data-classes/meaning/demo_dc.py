from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a: int           # <1>
    b: float = 1.1   # <2>
    c = 'spam'       # <3>

print(DemoDataClass.__annotations__)
print(DemoDataClass.__doc__)

dc = DemoDataClass(9)
print(dc)
print(dc.c)
dc.a = 5123
dc.z = 'secret stash'
print(dc.__dict__)