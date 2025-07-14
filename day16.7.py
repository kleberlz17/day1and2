from sys import getsizeof

#List e Generator Expressions
#Mais rápido para listas, dicionários e etc
#Menos memória alocada em bytes.

numeros = [x * 10 for x in range(1000)]
print(type(numeros))
print(getsizeof(numeros)) #Tamanho em bytes da lista.

numeros = (x * 10 for x in range(1000)) #Parenteses no lugar de [] pra
#tornar generator
print(type(numeros))
print(getsizeof(numeros)) #Tamanho em bytes da generator.