usuarios=[]

def validar_nome(nome):
    nome_valido=False 
    if len(nome)>=3:
        nome_valido=True
    else:
        print("Nome inválido! Curto demais.")
    return nome_valido

def validar_se_o_email_ja_ta_registrado(email):
    email_registrado=False
    for usu in usuarios:
        if(email==usu["email"]):
            print("O email já está registrado no sistema")
            print("Use outro email no cadastro")
            email_registrado=True
            
def validar_email(email):
    email_valido=False
    if("@" in email and ".com" in email):
        email_valido=True

def validar_senha(senha,senha2):
    senha_valida=False
    if(len(senha)>=6 and senha==senha2):
        senha_valida=True
    else:
        print("Senha invalida!Curta demais ou não coincidem")
        return senha_valida
        
        