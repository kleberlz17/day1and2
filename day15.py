# Listas e algumas funções
cidades = ["RJ", "SP", "MG", "RS"]

print(cidades)
print(cidades[0])
print(cidades[-4])
cidades[1] = "CWB" #Substitui index 1
cidades.append("RN") #Adiciona no fim da lista
cidades.remove("RS") # Remove
cidades.insert(1, "DF") # Coloca na posiçao(index) 1
cidades.pop(3) #Retira da lista pela posição
cidades.sort() #Ordem alfabetica
print(cidades)