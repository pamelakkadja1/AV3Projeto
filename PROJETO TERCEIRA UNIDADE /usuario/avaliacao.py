def avaliacoes_de_motorista(escolhamotorista):
    avaliacao_valida=False
    for car in cadastrodecarona:
        if(escolhamotorista in car["emaildomotorista"]):
            nota=input("Digite uma nota de 1 a 5: ")
            print("Avaliação feita com sucesso!")
            if len(nota)<=5:
                avaliacao_valida=True
        else:
            print("Esse motorista não é cadastrado!")
                