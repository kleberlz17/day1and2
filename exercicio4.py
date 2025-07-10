# Login Authentication
user = "admin"
password = 1234567

login = input("Digite o user: ")
login2 = int(input("Digite o password: "))

if login == user and login2 == password:
    print("Login OK")
else:
    print("Usuário ou senha incorretos.")

