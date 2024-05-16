menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numeros_de_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("Valor inválido!")

    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numeros_de_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Saldo insuficiente")

        elif excedeu_limite:
            print("Valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Número máximo de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numeros_de_saques += 1

        else:
            print("Valor inválido!")

    elif opcao == "e":
            print("\n============= EXTRATO =============")
            print("Não foi realizado movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("===================================")

    elif opcao == "q":
        break

    else:
        print("Selecione novamente a operação desejada.")
