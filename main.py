# MVC

# VIEW - o que vai para o usuário
usuario = input("Informe o usuário: ")
senha = input ("Informe a senha: ")

# MODEL - o que vem do BD
usuario_BD = "joao"
senha_BD = "123"

# CONTROLER - a validação
if usuario == usuario_BD and senha == senha_BD:
    print("pode entrar")
else:
    print ("usuário ou senha inválido")