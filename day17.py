#Erros - try e except (que deve ser sempre o erro que se espera)
#exemplo : se espera um int, value error se digitar SIM..

try:
    letras = ["a", "b", "c"]
    print(letras[3])
except IndexError:
    print("Index não existe")