import models.banco as banco
import views.formulario as view

def validar_login(usuario_digitado, senha_digitado):
    '''CONTROLLER - a validação'''
    validacao = usuario_digitado == banco.model_usuario() and senha_digitado == banco.model_senha() 
    if validacao:
        print("ACESSO PERMITIDO")
    else:
        print ("Usuário ou senha inválido")


def iniciar():
    view.formulario_login()