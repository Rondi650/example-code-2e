# import weakref
# s1 = {1, 2, 3}
# s2 = s1         
# def bye():      
#     print('...like tears in the rain.')

# ender = weakref.finalize(s1, bye)  
# print(ender.alive)  

# del s1
# print(ender.alive)  

# print(s2)
# s2 = 'spam'  

# print(ender.alive)

lista = [1, 2, 3]
print(f'conteudo da lista: {lista}')
print(f'id(lista): {id(lista)}')
lista.append(4)
print(f'conteudo da lista: {lista}')
print(f'id(lista): {id(lista)}')
lista += [5, 6]
print(f'conteudo da lista: {lista}')
print(f'id(lista): {id(lista)}')

print()   

lista1 = lista
print(f'id(lista1): {id(lista1)}')
lista1 += [7, 8]
print(f'conteudo da lista1: {lista1}')

print()

print(f'id(lista1): {id(lista1)}')
print(f'id(lista): {id(lista)}')
print(f'lista1 is lista: {lista1 is lista}')

print()

string = 'Hello'
print(f'id(string): {id(string)}')
string += ' world'
print(f'id(string): {id(string)}')
print(f'string: {string}')

open('test.txt', 'wt', encoding='utf-8').write('1, 2, 3')