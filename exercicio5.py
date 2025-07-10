#Desempenho escolar
nota = int(input("Digite a sua nota: "))

if nota >= 9:
    print("Excelente, você tirou um A.")
elif nota >= 7:
    print("Bom trabalho, você tirou um B.")
elif nota >= 5:
    print("Você passou, mas precisa melhorar. Você tirou um C.")
else:
    print("Você foi reprovado.")