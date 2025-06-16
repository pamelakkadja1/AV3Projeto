def arquivo_usuarios(usuarios):
        for chave,valor in usuarios:
            with open("usuarios.txt","a") as arquivousuarios:
                arquivousuarios.write(f"{chave}:{valor}\n")
        
    