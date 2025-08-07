#Comece solicitando o nome do usuário para "cadastrar" uma conta.
#Inicie o saldo dessa conta com R$ 0,00.

nome = input("Digite seu nome de usuário: ")
saldo = 0.00
print(f"Seu saldo é:R$ {saldo}")

#Execute um menu de operações de forma contínua, permitindo ao usuário escolher entre:
#Depositar: Adiciona um valor ao saldo.
#Sacar: Retira um valor do saldo (com a validação de que o saldo é suficiente).
#Listar Saldo: Exibe o saldo atual da conta.

opcao = ""
while opcao != "4":
    print("\n1. Depositar \n2. Sacar \n3. Saldo \n4. Sair")
    opcao = input("Opção: ")

    match opcao:
        case "1":
            saldo += float(input("Valor: "))
        case "2":
            valor = float(input("Valor: "))
            match valor <= saldo:
                case True:
                    saldo -= valor
                case False:
                    print("Você não tem essa quantia! Seu saldo:", saldo)
        case "3":
            print(f"Saldo: R$ {saldo:.2f}")
        case "4":
            print("Até logo", nome)
        case _:
            print("Opção inválida!")

#PESSIMO, NUNCA MAIS.