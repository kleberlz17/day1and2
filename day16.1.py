#Looping dentro de dicionário

aluno = {"nome": "Junior",
         "idade": 15,
         "média": 9.7,
         "aprovação": True}

for x in aluno.keys():
    print(x)

for x in aluno.values():
    print(x)

for keys, values in aluno.items(): #Tira os valores da {} mostrando keys e values
    print(keys, values)

print(len(aluno)) #Numero de keys