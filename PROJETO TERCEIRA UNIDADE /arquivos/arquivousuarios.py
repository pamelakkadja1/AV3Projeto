def arquivo_usuarios(usuarios):
    with open("usuarios.txt","a") as arquivousuarios:
        for chave,valor in usuarios.itens():
            arquivousuarios.write(f"{chave}:{valor}\n")
        
    