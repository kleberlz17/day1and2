#Controle de Temperaturas
temperatura = int(input("Digite a temperatura: "))

if temperatura < 10:
    print("Muito frio")
elif temperatura >=10 and temperatura < 20:
    print("Está fresco")
else:
    print("Está quente")
