#CATEGORIA PRODUTOS E OS PRODUTOS
# Este arquivo será uma lista de objetos, onde cada objeto representa uma categoria.
# Cada categoria deve ter um id_categoria (um número inteiro único) e um nome_categoria (texto).

#CATEGORIAS.JSON E PRODUTOS.JSON

import json

ARQUIVO_CATEGORIAS = 'categorias.json'
ARQUIVO_PRODUTOS = 'produtos.json'

categorias_id = 0
produtos_id = 0

categorias = []
produtos = []

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_arquivo(nome, dados):
    with open(nome, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def exibir_menu():
    print("\n--- Eletrônicos ---")
    print("[1] Cadastrar categoria")
    print("[2] Cadastrar produto")
    print("[3] Listar categorias")
    print("[4] Listar produtos")
    print("[5] Sair")

def cadastrar_categoria():
    global categorias_id
    global categorias
    
    nome_categoria = input("Nome da categoria: ")
    categoria = {"id": categorias_id, "nome": nome_categoria}
    categorias.append(categoria)
    salvar_arquivo(ARQUIVO_CATEGORIAS, categorias)
    categorias_id += 1

    print("Categoria cadastrada com sucesso!")

def cadastrar_produto():
    global produtos_id
    global produtos
    
    nome_produto = input("Nome do produto: ")
    preco = float(input("Preço: "))
    id_categoria = int(input("ID da categoria: "))
    produto = {
        "id": produtos_id,
        "nome": nome_produto,
        "preco": preco,
        "id_categoria": id_categoria
    }
    produtos.append(produto)
    salvar_arquivo(ARQUIVO_PRODUTOS, produtos)
    produtos_id += 1

    print("Produto cadastrado com sucesso!")

def listar_categorias():
    if categorias:
        print("CATEGORIAS:")
        for categoria in categorias:
            print(f"ID: {categoria['id']} - Nome: {categoria['nome']}")
    else:
        print("Nenhuma categoria cadastrada.")
        
def listar_produtos():
    if produtos:
        print("PRODUTOS:")
        for produto in produtos:
            nome_categoria = "Categoria não encontrada"
            for categoria in categorias:
                if categoria["id"] == produto["id_categoria"]:
                    nome_categoria = categoria["nome"]
                    break

            print(f"ID: {produto['id']} - Nome: {produto['nome']} - Preço: {produto['preco']} - Categoria: {nome_categoria}")
    else:
        print("Nenhum produto cadastrado.")

    #percorrer lista categoria
        #encontar categoria com id cadastrado no prod
        #pegar nome da categoria com chave  exemplo: categoria["nome"]

categorias = carregar_arquivo(ARQUIVO_CATEGORIAS)
produtos = carregar_arquivo(ARQUIVO_PRODUTOS)

while True:
    exibir_menu()
    opcao = input("Escolha: ")

    if opcao == '1':
        cadastrar_categoria()
    elif opcao == '2':
        cadastrar_produto()
    if opcao == '3':
        listar_categorias()
    elif opcao == '4':
        listar_produtos()
    elif opcao == '5':
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida.")