#Map em listas

lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

lista2 = map(multi, lista1)
print(list(lista2))

#Map com lambda

lista3 = map(lambda x: x * 2, lista1)
print(list(lista3))

#também
print(list(map(lambda x: x * 2, lista1)))
print(list(map(lambda x: x + 7, lista1)))