from random import randrange

from tombola import Tombola

from collections.abc import Sequence

from typing import Protocol, Tuple

@Tombola.register  # <1>
class TomboList(list):  # <2>

    def pick(self):
        if self:  # <3>
            position = randrange(len(self))
            return self.pop(position)  # <4>
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # <5>

    def loaded(self):
        return bool(self)  # <6>

    def inspect(self):
        return tuple(self)

# Tombola.register(TomboList)  # <7>

class RGB(Protocol):
    rgb: Tuple[int, int, int]

    @abstractmethod
    def intensity(self) -> int:
        return 0

class Point(RGB):
    def __init__(self, red: int, green: int, blue: str) -> None:
        self.rgb = red, green, blue  # Error, 'blue' must be 'int'

