import controllers.validacao as validacao

def formulario_login():
    '''VIEW - o que vai para o usuário'''
    usuario = input("Informe o usuário: ")
    senha = input ("Informe a senha: ")
    validacao.validar_login(usuario, senha)