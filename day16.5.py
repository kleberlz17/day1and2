#List Comprehension com Strings

frutas1 = ["abacate", "banana", "uva", "laranja", "abacaxi"]
#frutas2 = []

#for item in frutas1:
#    if "b" in item:
#        frutas2.append(item)

frutas2 = [item for item in frutas1 if "n" in item] 
print(frutas2)