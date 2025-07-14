#Filter = filtrar informações

valores = [17, 37, 47, 67, 77]

def mostrar20mais(x):
    return x > 20

print(list(filter(mostrar20mais, valores)))

#OU mais simplificado
#Ao invés da função, coloca um lambda
print(list(filter(lambda x: x > 20, valores)))