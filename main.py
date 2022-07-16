# EXEMPLO DE MVC

def view():
    '''VIEW - o que vai para o usuário'''
    usuario = input("Informe o usuário: ")
    senha = input ("Informe a senha: ")
    controller(usuario, senha)

def model_usuario():
    '''MODEL - o que vem do BD'''
    usuario_BD = "joao"
    return usuario_BD

def model_senha():
    '''MODEL - o que vem do BD'''
    senha_BD = "123"
    return senha_BD

def controller(usuario_digitado, senha_digitado):
    '''CONTROLLER - a validação'''
    validacao = usuario_digitado == model_usuario() and senha_digitado == model_senha() 
    if validacao:
        print("ACESSO PERMITIDO")
    else:
        print ("Usuário ou senha inválido")

view()