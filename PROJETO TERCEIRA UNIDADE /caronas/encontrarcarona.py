def encontrar_origem_destino(saidabusca,destinobusca):
    caronaencontrada=False
    for car in cadastrodecarona:
        if(saidabusca == car["origem"] and destinobusca == car["destino"]):
            caronaencontrada=True
            
def reservar_carona(escolhamotorista,escolhadata):
    caronaencontrada=False
    for car in cadastrodecarona:
        if(escolhamotorista in car["emaildomotorista"] and escolhadata in car["data"]):
            caronaencontrada=True

def encontar_por_data(escolhamotorista,dataprocurada):
    caronaencontrada=False
    for car in cadastrodecarona:
        if(dataprocurada in car["data"] 
        and escolhamotorista in car["emaildomotorista"]):
            caronaencontrada=True
        else:
            print("Não existe carona para essa data!")
