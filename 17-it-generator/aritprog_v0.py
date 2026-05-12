"""
Arithmetic progression class

    >>> ap = ArithmeticProgression(1, .5, 3)
    >>> list(ap)
    [1.0, 1.5, 2.0, 2.5]


"""


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> "infinite" series

    def __iter__(self):
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        forever = self.end is None
        while forever or result < self.end:
            yield result
            result += self.step


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    print(type(begin))
    print(type(result))
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index
        
ap = aritprog_gen(1,1.5,10)
print(list(ap))