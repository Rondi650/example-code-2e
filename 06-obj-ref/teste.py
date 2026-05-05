t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(f'id(t1): {id(t1)}')
print(f'id(t2): {id(t2)}')
print(f't1 == t2: {t1 == t2}')

print(f'id(t1[-1]): {id(t1[-1])}')

t1[-1].append(99)
print(f't1: {t1}')
print(f'id(t1[-1]): {id(t1[-1])}')

print(f't1 == t2: {t1[-1] == t2[-1]}')


print(f'id(t1): {id(t1)}')
print(f'id(t2): {id(t2)}')