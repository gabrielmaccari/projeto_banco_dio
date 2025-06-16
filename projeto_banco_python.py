menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nu] Novo usuario
[nc] Nova conta
[lc] Listar contas
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios=[]
contas=[]

def saque(*,saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Sacou: R$ {valor:.2f}\n"
        numero_saques += 1


    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depositou: R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    else:
        print("Operacao falhou! O valor informado e invalido!")

    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return saldo,extrato

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF sem os pontos ou traços:")
    usuario=filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Já existe um usuário com este CPF")
        return
    nome=input("Informe o seu nome:")
    data_nascimento=input("Informe sua data de nascimento:")
    endereco = input("Informe o seu endereço(logradouro - número - bairro - cidade/estado)")
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "endereco":endereco, "cpf":cpf})
    print("Usuário cadastrado com sucesso!")



def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
        else:
            return False

def criar_conta(agencia, numero_conta, usuarios):
    cpf=input("Digite o CPF:")
    usuario=filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": cpf}
    else:
        print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha =f"""
        Agência: {conta["agencia"]}
        Número da conta: {conta["numero_conta"]}
        Titulares: {conta["usuario"]}
"""
        print(linha)

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato=depositar(saldo,valor,extrato)


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES)


    elif opcao == "e":
        saldo, extrato = exibir_extrato(saldo,extrato=extrato)

    elif opcao == "q":
        break

    elif opcao == "nu":
        user = criar_usuario(usuarios)
        usuarios.append(user)

    elif opcao=="nc":
        conta = criar_conta("0001", len(contas)+1, usuarios)

        if conta:
            contas.append(conta)
    elif opcao=="lc":
        listar_contas(contas)

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")