#Nested Loops
for numero1 in range(1,6):
    print("Produto " + str(numero1))
    for numero2 in range(11):
        print(numero1, numero2)

##############################################

palavra = "CENTURIES"

for espaco in palavra:
    print(f" {espaco}" , end="") ##Precisa de um espaço entre o f" e {espaco}