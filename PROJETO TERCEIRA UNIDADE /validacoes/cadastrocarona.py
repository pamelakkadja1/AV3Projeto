def validar_placa_do_veiculo(placa):
    placavalida=False
    if len(placa)==7:
        placa_valida=True
    else:
        print("Placa invalida!Não é padrão do mercosul")
        print("Escreva-a corretamente agora!")
        
def validar_vaga(vagas):
    vaga_valida=False
    if (vagas>0 and "-" not in vagas):
        vagavalida=True
    else:
        print("Digite corretamente")

def validar_valor_por_vaga(valorporVaga):
    valor_por_vaga_valido=False
    if(valorporVaga>0 and "-" not in valorporVaga):
        valor_por_vaga_valido=True
    else:
        print("Digite corretamente")
        

def validar_horario_carona(horario):
    horario_valido=False
    if ":" in horario:
        horario_valido=True
    else:
        print("Horário invalido!")
        print("Tente novamente!")
        
def validar_data(data):
    data_valida=False
    dia= data[0:1]
    mes= data[3:4]
    ano= data[6:10]
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    if(dia>0 and mes==meses and ano=="2025"):
        data_valida=True

def validar_tipo_veiculo(tipoveiculo):
    tipo_de_veiculo_valido=False
    if(tipoveiculo=="carro" and tipoveiculo=="moto"):
        tipo_de_veiculo_valido=True


    
    
    