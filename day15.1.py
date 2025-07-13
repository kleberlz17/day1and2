#Concatenando listas


numeros = [2, 3, 4, 5]
letras = ["a", "b", "c", "d"]

numeros.extend(letras)
print(numeros)

itens = [[2, 3, 4, 5], [6, 7, 8, 9]]
print(itens[1][1]) #lista 1 index 1 = 7