def procura_de_data01(dataprocurada):
    data_valida=False
    dia= dataprocurada[0:1]
    mes= dataprocurada[3:4]
    ano= dataprocurada[6:10]
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    if(dia>0 and mes==meses and ano=="2025"):
        data_valida=True
