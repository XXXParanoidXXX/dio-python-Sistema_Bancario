#By Vinícius Lima (Paranoid)
#Sistema bancário em Python criado em 21/09/2024.

def main():
    saldo = 0
    limite_saque = 500
    saques_diarios = 3
    num_saques = 0
    extrato = []

    while True:
        print("""
        ==================== MENU ====================
        1 - Depósito
        2 - Saque
        3 - Extrato
        4 - Sair
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido para depósito.")
        
        elif opcao == '2':
            if num_saques >= saques_diarios:
                print("Limite de saques diários atingido.")
            else:
                valor = float(input("Digite o valor para saque: R$ "))
                if valor > saldo:
                    print("Saldo insuficiente.")
                elif valor > limite_saque:
                    print(f"O limite por saque é de R$ {limite_saque:.2f}.")
                elif valor > 0:
                    saldo -= valor
                    num_saques += 1
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Valor inválido para saque.")
        
        elif opcao == '3':
            print("\n====== EXTRATO ======")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for movimento in extrato:
                    print(movimento)
                print(f"\nSaldo atual: R$ {saldo:.2f}")
        
        elif opcao == '4':
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
