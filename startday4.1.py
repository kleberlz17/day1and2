#Taxa de 10% sobre o produto.
valor = float(input("Digite o valor do produto: "))
percentual = 10
valor_percentual = valor * (percentual / 100)
print(valor + valor_percentual)

# Poderia ser também :

valor_com_acrescimo = valor * 1.10
print(f"O valor com acréscimo é de: R$ {valor_com_acrescimo:.2f}")