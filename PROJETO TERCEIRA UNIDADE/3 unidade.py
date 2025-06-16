from validacoes.validacaocadastro import validar_nome
from validacoes.validacaocadastro import validar_se_o_email_ja_ta_registrado
from validacoes.validacaocadastro import validar_email
from validacoes.validacaocadastro import validar_senha
from validacoes.cadastrocarona import validar_placa_do_veiculo
from validacoes.validacaologin import login_do_usuario
from validacoes.cadastrocarona import validar_vaga
from validacoes.cadastrocarona import validar_valor_por_vaga
from validacoes.cadastrocarona import validar_horario_carona
from validacoes.cadastrocarona import validar_data
from validacoes.cadastrocarona import validar_tipo_veiculo
from caronas.listarcarona import listagem_carona
from validacoes.procuradedata import procura_de_data01
from caronas.encontrarcarona import encontrar_origem_destino
from caronas.encontrarcarona import reservar_carona
from caronas.encontrarcarona import encontar_por_data
from caronas.removercarona import remover_carona
from caronas.removerreserva import remover_reserva
from usuario.avaliacao import avaliacoes_de_motorista
from arquivos.arquivousuarios import arquivo_usuarios




usuarios=[]
arquivo_usuarios(usuarios)
usuariologado={}
cadastrodecarona=[]
reserva=[]
avaliaçoes=[]

print("      ______")
print("  ___//__|__\\___")
print(" |  _   _   _    |")
print(" '-(_)--(_)---(_)-'")

print("========CAJAZEIRAS CARONAS=========")

while True:
    print("========MENU DE CADASTRO========")
    opcao=input("ESCOLHA O QUE VOCÊ DESEJA FAZER\n\n"
                "0 - Sair do aplicativo\n"\
                "1 - Cadastro do usuário\n"\
                "2 - LOGIN\n"\
                "\nDIGITE A OPÇÃO ESCOLHIDA : ")
    
    if(opcao=="0"):
        print("Até a proxima!")
        break

    elif(opcao=="1"):
        print("========CADASTRO========")
        
        while True:
            nome=input("Digite o seu nome: ")
            if validar_nome(nome)==True:
                break
            
        while True:
            email=input("Digite seu email: ")
            if (validar_se_o_email_ja_ta_registrado(email)==True 
            and validar_email(email)==True):
                break
            
        while True:
            senha=input("Digite sua senha: ")
            senha2=input("Confirme sua senha: ")
            if validar_senha(senha,senha2)==True:
                break
            
            
        usuarios.append({"nome":nome,
                        "email":email,
                        "senha":senha
                    })
        
        print("Cadastro feito com sucesso!!")
        print("=" * 32)
        
    elif(opcao=="2"):
        print("=======LOGIN=========")
        while True:
            email =input("Digite o seu email: ")
            senha=input("Digite sua senha: ")
            if login_do_usuario(login)==True:
                break
            
        while(login==True):
            print("========MENU DE LOGIN=========")
            opcao2=input("ESCOLHA O QUE DESJA FAZER\n\n"
                    "0 - Logout\n"\
                    "1 - Cadastro de carona\n"\
                    "2 - Lista de caronas disponiveis\n"\
                    "3 - Buscar carona por origem e destino\n"\
                    "4 - Buscar por data\n"\
                    "5 - Reserva de Carona\n"\
                    "6 - Minhas caronas\n"\
                    "7 - Remoção de Carona\n"\
                    "8 - Cancelar reserva\n"\
                    "9 - Avaliar motorista\n"\
                    "10 - Relatorio\n"
                    "\nDIGITE O QUE ESCOLHEU: ")

            if(opcao2=="0"):
                print("Até mais!")
                break
                
            elif(opcao2=="1"): 
                print("Informe as seguintes informaçoes!")
                nomedomotorista=usuariologado["nome"]
                emaildomotorista=usuariologado["email"]
                
                while True:
                    tipoveiculo=input("Digite o tipo do veiculo(moto ou carro): ").lower()
                    if validar_tipo_veiculo(tipoveiculo)==True:
                        break
                
                nomedoveiculo=input("Digite o nome do veiculo (Onix,Prisma, POP100):")
                cordoVeiculo=input("Digite a cor do veiculo: ")
                
                while True:
                    placa=input("Digite a placa do veiculo :").upper()
                    if validar_placa_do_veiculo(placa)==True:
                        break
                    
                origem=input("Digite de onde o veiculo vai sair : ")
                destino=input("Digite o destino da viagem: ")
                
                while True:
                    vagas=int(input("Digite quantas vagas tem  no veiculo : "))
                    if validar_vaga(vagas)==True:
                        break
                    
                while True:
                    valorPorVaga = float(input("Digite o valor por cada vaga : "))
                    if validar_valor_por_vaga(valorporVaga)==True:
                        break
                
                while True:
                    horario=(input("Digite o horario da viagem (10:00) : "))
                    if validar_horario_carona(horario)==True:
                        break
                    
                while True:
                    data=input("Digite a data da viagem (Formarto em dd/mm/aaaa): ")
                    if validar_data(data)==True:
                        break
                    
                cadastrodecarona.append({"nomedomotorista":nomedomotorista,
                                                "emaildomotorista":emaildomotorista,
                                                "tipoveiculo":tipoveiculo,
                                                "nomedoveiculo":nomedoveiculo,
                                                "cordoveiculo":cordoVeiculo,
                                                "placa":placa,
                                                "origem":origem,
                                                "destino":destino,
                                                "data":data,
                                                "horario":horario,
                                                "vagas":vagas,
                                                "valorporVaga":valorPorVaga})
                
                print("Carona cadrastada com sucesso!!!")
                
            elif(opcao2=="2"):
                print("="*32)
                print("\nLista de Caronas\n")
                listagem_carona(cadastrodecarona)
                print("="*32)
                
            elif(opcao2=="3"):
                    saidabusca=input("Digite de onde vai sair: ") 
                    destinobusca=input("Digite para onde voce quer ir: ")
                    if encontrar_origem_destino(saidabusca,destinobusca)==True:
                        print("Encontrou uma carona!\n\n")
                        print("=" * 36)
                        listagem_carona(cadastrodecarona)
                        print("=" * 36)
                        
            elif(opcao2=="5"):
                while True:
                    escolhamotorista=input("Digite o email do motorista desejado:")
                    escolhadata=input("Digite a data da carona (dd/mm/aaaa): ")
                    if encontrar_data01(escolhadata)==True:
                        print("Carona encontrada!")
                        listagem_carona(cadastrodecarona)
                        if(car["vagas"]>0):
                            escolha=input("Deseja realmente reservar? (s/n): ").lower()
                            if(escolha=="s"):
                                car["vagas"]-=1
                                reserva.append({"emailpassageiro": usuariologado,
                                                "emailmotorista": escolhamotorista,
                                                "data": escolhadata})
                                print("Reserva feita com sucesso!")
                                break
                            else:
                                print("Reserva cancelada.")
                        else:
                            print("Essa carona não tem mais vagas.")
                            
                    else:
                        print("Carona inexistente!")
                            
            elif(opcao2=="6"):
                print("Caronas cadastradas")
                for car in cadastrodecarona:
                    if(emaildomotorista==usuariologado["email"]):
                        listagem_carona(cadastrodecarona)
                print("="*18)
                    
            elif(opcao2=="4"):
                escolhamotorista=input("Digite o email do motorista desejado:")
                dataprocurada=input("Digite uma data (dd/mm/aaaa): ")
                if encontrar_por_data(escolhamotorista,escolhadata)==True:
                    print("Carona encontrada!")
                    listagem_carona(cadastrodecarona)
                    
            elif(opcao2=="7"):
                while True:
                    emaildomotorista=input("Digite o seu email: ")
                    senha3=input("Digite a sua senha:")
                    dataprocurada2=input("Digite a data da carona(dd/mm/aaaa): ")
                    if remover_carona(emaildomotorista,senha3,dataprocurada2)==True:
                        break
                    
            elif(opcao2=="8"):
                while True:
                    escolhamotorista=input("Digite o email do motorista: ")
                    dataprocurada3=input("Digite a data da carona(dd/mm/aaaa):")
                    if remover_reserva(escolhamotorista,dataprocurada3)==True:
                        break
                    
                            
            elif(opcao2=="9"):
                while True:
                    escolhamotorista=input("Digite o email do motorista que voce quer avaliar: ")
                    if avaliacoes_de_motorista(escolhamotorista)==True:
                        break
                    
                    avaliaçoes.append({"motorista":escolhamotorista,
                                "nota":nota})
            elif(opcao2=="10"):
                if(emaildomotorista==usuariologado):
                    with open("relatorio.txt","a") as arquivorelatorio:
                        arquivorelatorio.write(cadastrodecarona)
                    
            