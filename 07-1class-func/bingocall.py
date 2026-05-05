"""
# tag::BINGO_DEMO[]

>>> bingo = BingoCage(range(3))
>>> bingo.pick()
1
>>> bingo()
0
>>> callable(bingo)
True

# end::BINGO_DEMO[]

"""

# tag::BINGO[]

import random


class BingoCage:

    def __init__(self, items):
        print(f'items: {items}')
        self._items = list(items)  # <1>
        random.shuffle(self._items)  # <2>

    def pick(self):  # <3>
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # <4>

    def __call__(self):  # <5>
        return self.pick()

# end::BINGO[]


def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(map(factorial, range(11)))
print(list(map(factorial, range(11))))

bingo = BingoCage(range(3))
print(bingo)
print(bingo.pick())
print(bingo())

print(list(range(3)))