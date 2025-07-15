##### Try e except com Input

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Por favor, digite o valor em numeros.")