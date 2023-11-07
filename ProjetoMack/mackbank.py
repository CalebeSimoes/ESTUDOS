import random



#Variavel trava caso não tenha cadastro
verificaOP = False

#Variavel dados do cliente
nomecliente = ()
saldocliente = 0
telefonecliente = 0
emailcliente = ()
numeroDaConta = random.randint(1000,9999)




def cadastro():
    print("MACK BANK – CADASTRO DE CONTA\nO numero da sua conta é:", numeroDaConta)
    global saldocliente
    global nomecliente
    global emailcliente
    global telefonecliente

    telefonecliente = telefonecliente.replace(" ","").replace("-","")
    if len(telefonecliente) <= 11:
        print(f"{telefonecliente} é um numero invalido para cadastro.")

        elif len(telefonecliente) >= 11:
            print(f"{telefonecliente} é um numero invalido")
    
    
    nomecliente = input("NOME DO CLIENTE: ")
    telefonecliente = int(input("TELEFONE.......: "))
    emailcliente = input("EMAIL..........: ")
    saldocleinte = float(input("SALDO INICIAL...: "))



    if saldocliente < 1000:
        print("Saldo insuficiente para criação da conta!")
     

    limitecliente = float(input("LIMITE DE CRÉDITO: "))


    senhacliente = int(input("SENHA............: "))



    print("CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")


def menu():
    print("MACK BANK – ESCOLHA UMA OPÇÃO\n(1) CADASTRAR CONTA CORRENTE\n(2) DEPOSITAR\n(3) SACAR\n(4) CONSULTAR SALDO\n(5) CONSULTAR EXTRATO\n(6) FINALIZAR")
    global escolha
    escolha = int(input("SUA OPÇÃO: "))


    if escolha == 1:
        cadastro()
        print("cadastro")
        global verificaOP
        verificaOP = True


    elif escolha == 2:
        if verificaOP == True:
            #def deposito
            print("deposito")
        else:
            print("escolha 2 caiu no else")

    elif escolha == 3:
        if verificaOP == True:
            #def sacar
            print("sacar")
        else:
            print("escolha 3 caiu no else") 

    elif escolha == 4:
        if verificaOP == True:
            #def consultar saldo
            print("saldo")
        else:
            print("escolha 4 caiu no else")

    elif escolha == 5:
        if verificaOP == True:
            #def consultar extrato
            print("extrato")
        else:
            print("escolha 5 caiu no else")

    elif escolha == 6:
        print("finalizar")
menu()









