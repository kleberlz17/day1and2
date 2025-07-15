#Try e except com else e finally.

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Por favor, digite o valor em numeros.")
else: ##Só aparece se o try der Ok
    print("Usuario digitou um valor corretamente.")
finally: ## Aparece, indiferente se o try der ok ou cair no except.
    print("codigo ok")