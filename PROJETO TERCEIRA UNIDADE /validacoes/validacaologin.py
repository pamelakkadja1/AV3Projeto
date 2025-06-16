def login_do_usuario (email,senha):
    login=False
    for usu in usuarios:
        if(email==usu["email"] and senha==usu["senha"] ):
            login=True
            usuariologado=usu
            print("Login efetuado com sucesso!!")
            break
        else:
            print("Erro no login,algo está errado!") 

