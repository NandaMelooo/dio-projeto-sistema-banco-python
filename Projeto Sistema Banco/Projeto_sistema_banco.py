#Projeto de sistema bancário - V_01#

menu = """"
    ######## MENU ########

    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [q]  Sair
    \n######################
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor a ser depositado:"))

        if valor > 0:                          
            saldo  += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
         print("Operação falhou! Ovalor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe valor do saque:"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
             print("Operação falhou! Valor solicitado excede o limite.")

        elif excedeu_saques:
             print("Operação falhou! Operação excede os limites de saque.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falou! Valor informado é inválido.")

    elif opcao == "e":
        print("\n########### Extrato ############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n######################################")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação.")