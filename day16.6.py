#List Comprehension com números
#Com for loop injetando os numeros na lista.

numeros = []

for x in range(6): #Fora da lista, padrão
    numeros.append(x * 10) #De 10 em 10, x é vazio
print(numeros)

valores = [x * 10 for x in range(6)] #For loop já dentro da lista
print(valores)
