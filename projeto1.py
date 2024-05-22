import os

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return (input(menu)).lower()

def depositar(valor, saldo, extrato):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f'=== Depósito realizado com sucesso ===')

        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, limite_saques, numero_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f'=== Saque realizado com sucesso ===')

        else:
            print("Operação falhou! O valor informado é inválido.")
        
        return saldo, extrato

def exibir_extrato(saldo, /, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
 

def main():
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato) 
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                numero_saques = numero_saques,
                extrato=extrato,
                saldo=saldo,
                valor=valor,
                limite = limite,
                limite_saques = LIMITE_SAQUES
                ) 
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            os.system('cls')
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()