# Condições (If - Else - Elif) Se - Se não - Ou
idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 60:
    print("Maior de idade")
else:
    print("Idoso")

