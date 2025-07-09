#Entrada
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: ")) #Sem o int, a idade sai como str(string) | foi convertido
# int() float() bool() str(), todos são possiveis.
pais = input("Digite o país onde mora: ")
print(f"Olá, {nome}! Seja bem-vindo! Você possui {idade} anos de idade e mora no {pais}!")


print(type(nome))
print(type(idade))