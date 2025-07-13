#Sets com strings

set1 = {"k", "l", "f", "m"}
set2 = {"y", "k", "l", "c"}

unificarsets = set1.union(set2) #Unifica os 2 sets.
diferencasets = set1.difference(set2) #Diferença entre o set 1 ao 2.
igualsets = set1.intersection(set2) #Igual no set 1 em relação ao 2.
print(unificarsets)
print(diferencasets)
print(igualsets)
