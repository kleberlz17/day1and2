#Unpacking Lists e loop dentro da lista

produtos = ["arroz", "feijao", "maçã", "laranja"]
item1, item2, item3, *outro = produtos
print(item1, item2, item3, outro)

valores = [50, 70, 90, 200]
for x in valores:
    print(f" O valor final do produto é de R${x}.")