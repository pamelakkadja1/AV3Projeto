def listagem_carona(cadastrocarona):
    for car in cadastrodecarona:
        if(car["vagas"]>0):
            print(f"Nome do motorista : {car["nomedomotorista"]}")
            print(f"Email do motorista:{car["emaildomotorista"]} ")
            print(f"Veiculo: {car["tipoveiculo"]}")
            print(f"Nome do veiculo: {car["nomedoveiculo"]}")
            print(f"Cor do veiculo: {car["cordoveiculo"]}")
            print(f"A placa do veiculo: {car["placa"]}")
            print(f"Saída da viagem : {car["origem"]}")
            print(f"Destino da viagem: {car["destino"]}")
            print(f"Data da viagem : {car["data"]}")
            print(f"Horário da viagem :{car["horario"]}")
            print(f"Vagas disponiveis: {car["vagas"]}")
            print(f"Valor por vaga: {car["valorporVaga"]}")
    print("="*32)