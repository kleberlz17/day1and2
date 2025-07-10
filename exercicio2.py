#Saudações
horario = int(input("Digite o horário: "))

if horario < 12:
    print("Bom dia")
elif horario < 18 and horario >= 12:
    print("Boa tarde")
else:
    print("Boa noite")