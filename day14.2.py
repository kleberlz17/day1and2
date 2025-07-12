#Simplificando a função
#Default = quantidade = Parametro já definido na função.
#Regra = Default é sempre no final.

def welcome(nome, quantidade=7):
    print(f"Olá {nome} , bem vindo ao nosso site.")
    print(f"Temos {str(quantidade)} laptops em estoque")

welcome("Junior")