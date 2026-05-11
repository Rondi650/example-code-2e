# tag::CAST[]
from typing import cast

def find_first_str(a: list[object]) -> str:
    index = next(i for i, x in enumerate(a) if isinstance(x, str))
    # We only get here if there's at least one string
    return cast(str, a[index])
# end::CAST[]


from typing import TYPE_CHECKING

l1 = [10, 20, 'thirty', 40]
if TYPE_CHECKING:
    reveal_type(l1)

print(find_first_str(l1))

l2 = [0, ()]
try:
    find_first_str(l2)
except StopIteration as e:
    print(repr(e))


x = 1
print(type(cast(str, x)))
print(type(x))



class Animal: ...
class Cachorro(Animal): ...  # Cachorro é subtipo de Animal
from typing import Callable

def retorna_animal() -> Animal:
    return Animal()

def retorna_cachorro() -> Cachorro:
    return Cachorro()

# Covariante: onde se espera "retorna Animal", aceita "retorna Cachorro"
# porque Cachorro é Animal — faz sentido
handler: Callable[[], Animal] = retorna_cachorro  # ✅ ok



def processa_animal(a: Animal) -> None:
    print(a)

def processa_cachorro(c: Cachorro) -> None:
    print(c)

# Contravariante: onde se espera "aceita Cachorro", prefere "aceita Animal"
# porque uma função que aceita qualquer Animal aceita Cachorro também
handler1: Callable[[Cachorro], None] = processa_animal  # ✅ ok
handler2: Callable[[Cachorro], None] = processa_cachorro  # ✅ ok
handler3: Callable[[Animal], None] = processa_cachorro    # ❌ não seguro