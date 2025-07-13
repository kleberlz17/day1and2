#Verificando itens em uma lista
cor_cliente = input("Digite a cor desejada: ")
cores = ["amarelo", "verde", "azul", "vermelho"]

if cor_cliente.lower() in cores: #Coloca em lower caso digite com letra maiuscula
    print("Em estoque")
else:
    print("Não temos essa cor em estoque")