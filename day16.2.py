#Lambda

somar = lambda x, y: x + y + 7 #Defini 2 argumentos, então espera 2 argumentos.
print(somar(7, 7))

##Lambda dentro de uma função

def somar(x):
    func2 = lambda x: x + 7  # 1 + 7 = 8
    return func2(x) * 4  # 8 * 4 = 32

print(somar(1)) # valor do x da função somar = 1

