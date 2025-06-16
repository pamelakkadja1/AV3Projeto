def remover_reserva(escolhamotorista,dataprocurada3):
    reservaremovida=False
    for r in reserva:
        if(r["emailpassageiro"]==usuariologado["email"]
        and dataprocurada3 == r["data"]
        and escolhamotorista == r["emailmotorista"]):
            reserva.remove(r)
            for car in cadastrodecarona:
                if(car["emaildomotorista"]==emaildomotorista
                and car["data"]==dataprocurada3):
                    car["vagas"]+=1
                    print("Reserva cancelada com sucesso!!")
                    reservaremovida=True