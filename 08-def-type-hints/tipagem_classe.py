from typing import Any

class T1:
    ...

class T2(T1):
    ...

def f1(p: T1) -> None:
    ...

o2 = T2()

f1(o2)  # OK

# ------------------

def f2(p: T2) -> None:
    ...

o1 = T1()

f2(o1)  # type error

# ------------------

def f3(p: Any) -> None:
    ...

o0 = object()
o1 = T1()
o2 = T2()

f3(o0)  #
f3(o1)  #  tudo certo: regra #2
f3(o2)  #

def f4():  # tipo implícito de retorno: `Any`
    ...

o4 = f4()  # tipo inferido: `Any`

f1(o4)  #
f2(o4)  #  tudo certo: regra #3
f3(o4)  #

ord