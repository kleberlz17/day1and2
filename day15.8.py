#Sets (Listas)
#Perde a indexação (fica fora de ordem)

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # | retira os repetidos.
print(num1 - num2) #Mostra diferença da num1 em relação a num2
print(num1 ^ num2) #Retira os duplicados.
print(num1 & num2) #Mostra os duplicados.

print(len(num1)) #Quantidade de itens na lista.

