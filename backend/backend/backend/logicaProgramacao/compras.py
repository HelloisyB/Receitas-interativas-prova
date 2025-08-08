#cadastrar produto, excluir produto, listar produto.
#MENU DE OPERAÇÕES, USO DE LISTA, MATCH CASE, USAR FUNÇÃO (obrigatorio)
#aceitar letras A | a .upper ( string de texto em letras maiúsculas) e minusculos

produtos = []

#Menu
def menu():
    print("MENU")
    print("1. Cadastrar")
    print("2. Excluir")
    print("3. Listar")
    print("4. Sair")
    return input("Escolha uma opção de 1 a 4: ")

#cadastrar
def cadastrar(produtos):
    nome = input("Digite o nome do produto para cadastro: ").upper()
    if nome:
        produtos.append(nome)
        print("Produto cadastrado com sucesso!")
    else:
        print("Nenhum produto informado.")

#excluir
def excluir(produtos):
    nome = input("Digite o nome do produto para excluir: ").upper()
    if nome in produtos:
        produtos.remove(nome)
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")

#lista
def listar(produtos):
    if produtos:
        print("PRODUTOS CADASTRADOS:")
        for produto in produtos:
            print("Produto:", produto)
    else:
        print("Nenhum item cadastrado.")

#match
while True:
    opcao = menu()

    match opcao:
        case "1":
            cadastrar(produtos)
        case "2":
            excluir(produtos)
        case "3":
            listar(produtos)
        case "4":
            print("Saindo do programa.")
            break
        case _:
            print("Tente novamente.")
