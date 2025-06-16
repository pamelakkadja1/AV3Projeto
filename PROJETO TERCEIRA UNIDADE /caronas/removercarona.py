def remover_carona(emaildomotorista,senha3,dataprocurada2):
    caronaremovida=False
    for car in cadastrodecarona:
        if(emaildomotorista==usuariologado["email"]
        and dataprocurada==car["data"]
        and senha3==usuariologado["senha"]):
            cadastrodecarona.remove(car)
            print("Carona removida com sucesso!!")
            caronaremovida=True
        else:
            print("Voce nao pode remover uma carona!")                