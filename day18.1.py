from datetime import datetime
from traceback import print_tb


class Funcionarios:

##Construtor em python (self é o objeto = usuario1/usuario2...)
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + " " + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento



usuario1= Funcionarios("Junior", "Luiz", 2007)
usuario2 = Funcionarios("Eduardo", "Ricardo", 2003)

print(Funcionarios.nome_completo(usuario2))
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
