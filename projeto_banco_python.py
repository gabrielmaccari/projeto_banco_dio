print("""
================================
       MENU DO CAIXA
    [0] DEPÓSITO
    [1] SAQUE
    [2] EXTRATO
    [3] SAIR
================================
""")
saldo=0
extrato=""
limite=500
LIMITE_SAQUES=3
numero_saques=0

while True:
    opcao=int(input("Qual alternativa deseja?:"))

    if opcao==0:
        valor=float(input("Quanto deseja depositar?:"))
        if valor>0:
            saldo+=valor
            extrato+=f"Depósito de R${valor:.2f}\n"
        else:
            print("Valor incorreto, digite novamente!")
    elif opcao==1:
        saque=float(input("Quanto deseja sacar?:"))
        if saque>500:
            print("Não é possível realizar saques maiores que R$500,00 reais.")
        else:
            while numero_saques<LIMITE_SAQUES:
                numero_saques+=1
                extrato+=f"Saque de R${saque:.2f}\n"
                print(f"Foi realizado um saque de R${saque} reais, você ainda tem {LIMITE_SAQUES-numero_saques} saques para fazer hoje")
                break
            else:
                print("Você realizou o máximo de saques por hoje")
    elif opcao==2:
        print(extrato)
    elif opcao==3:
        print("Obrigado por usar nosso sistema")
        break
                
        
    