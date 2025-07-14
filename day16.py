#Dicionários

aluno = {"nome": "Junior", "idade": 15, "média": 9.7, "aprovação": True}
print(aluno["média"])

aluno["nome"] = "Bruce"
print(aluno)

aluno.update({"média": 10, "idade": 16, "endereço": "Rua XYZ"})
print(aluno)

del aluno["endereço"]
print(aluno)