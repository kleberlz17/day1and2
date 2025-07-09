mensagem = "  TEst tESt teSTando tEst tesT"

#Indexação e Fatiamento
print(mensagem[1]) # Pega o "e" da mensagem
print(mensagem[0:3]) # Vai do 0 ao 2. "tes"
print(mensagem[-3:])

#Metodos comuns em Strings
print(mensagem.upper()) # Uppercase
print(mensagem.lower()) # Lowercase
print(mensagem.strip()) # Remove espaços em branco
print(mensagem.replace("teSTando", "test")) # Substitui
print(mensagem.split()) # Textos entre []

#Formatação F-string
nome = "Kleber Luiz"
idade = 26
print(f"O meu nome é {nome} e eu tenho {idade} anos de idade")

# Escape Sequence = \n - \t
mensagem2 = "c:\\Users\\Junior" #Pra mostrar caminho tem que colocar 2 //
print(mensagem2)

mensagem3 = "Nome:\tJunior\nIdade:\t26\nPaís:\tBrasil"
mensagem4 = "Coração: \u2764"
print(mensagem3)
print(mensagem4)

