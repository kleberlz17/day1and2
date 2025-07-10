#Descontos na compra
valor = float(input("Digite o valor da compra: "))

if valor > 200:
    desconto = 0.2
elif valor > 100:
    desconto = 0.1
else:
    desconto = 0.05

valor_final = valor - (valor * desconto)
print(f"O valor final com desconto é de R${valor_final:.2f}")