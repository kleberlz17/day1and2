#Função que soma vários numeros. varios argumentos(xargs)
#Com uso de for loop

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


x = soma(2, 3, 4, 7, 7)
print(x)