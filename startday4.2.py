# Multiplas entradas na mesma linha de Input()

dados = input("Digite o seu nome, idade e altura: ").split() #Separa os espaços (index)
nome = dados[0] # nome é index 0
idade = dados[1] # idade é index 1
altura = dados[2] # altura é index 2

print(f"Seu nome é {nome.upper()}, você possuí {idade} anos de idade e tem {altura} de altura.")
