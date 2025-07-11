#For Loops
from operator import truediv

for numero in range(1, 8):
    print(numero)

for letra in "Google":
    print(letra)
##################################################
compra_confirmada = True
dados_compra = "Compra no valor de R$12.75."

for enviar in range(3): #3 tentativas
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviados para o seu email")
        break
else:
    print("Falha na compra")