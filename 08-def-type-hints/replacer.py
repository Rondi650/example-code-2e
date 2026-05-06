"""
``zip_replace`` replaces multiple calls to ``str.replace``::

    >>> changes = [
    ...     ('(', ' ( '),
    ...     (')', ' ) '),
    ...     ('  ', ' '),
    ... ]
    >>> expr = '(+ 2 (* 3 7))'
    >>> zip_replace(expr, changes)
    ' ( + 2 ( * 3 7 ) ) '

"""

# tag::ZIP_REPLACE[]
from collections.abc import Iterable

FromTo = tuple[str, str]  # <1>

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:  # <2>
    for from_, to in changes:
        print(from_, '->', to)  # <3>
        text = text.replace(from_, to)
    return text
# end::ZIP_REPLACE[]

def demo() -> None:
    import doctest
    failed, count = doctest.testmod()
    print(f'{count-failed} of {count} doctests OK')
    l33t = [(p[0], p[1]) for p in 'a4 e3 i1 o0'.split()]
    print(l33t)
    text = 'mad skilled noob powned leet'
    print(zip_replace(text, l33t))


if __name__ == '__main__':
    demo()

string = 'mad'
string = string.replace('a', '4')
print(string)  # 'm4d'