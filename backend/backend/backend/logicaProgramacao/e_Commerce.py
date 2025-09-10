#CATEGORIA PRODUTOS E OS PRODUTOS
# Este arquivo será uma lista de objetos, onde cada objeto representa uma categoria.
# Cada categoria deve ter um id_categoria (um número inteiro único) e um nome_categoria (texto).

#CATEGORIAS.JSON E PRODUTOS.JSON

import json

ARQUIVOS_CATEGORIAS = 'categorias.json'
ARQUIVOS_PRODUTOS = 'produtos.json'
categorias_id = 1
produto_id = 1

categorias = []
produtos = []

def carregar_arquivo(eletronico):
    try:
        with open(eletronico, 'r') as arquivo:
            dados = json.load(arquivo)
            print(f"Arquivo {eletronico} carregado!")
            return dados
    except FileNotFoundError:
        print(f"Arquivo não encontrado. Criando novo arquivo.")
        return []

def salvar_arquivo(nome_eletronico):
    with open(nome_eletronico, 'w') as arquivo:
        json.dump(arquivo, indent=4)
    print(f"Arquivo salvo com sucesso!")

def exibir_menu():
    print("\n--- Eletrônicos ---")
    print("[1] Cadastrar categoria")
    print("[2] Cadastrar produto")
    print("[3] Alterar produto")
    print("[4] Excluir produto")
    print("[5] Listar categorias")
    print("[6] Listar produtos")
    print("[7] Sair")

def cadastro():
    nome = input("Nome da nova categoria: ")
    novo_id = categorias_id(categorias, "categoria_id")
    nova_categoria = {
        "categoria_id": categorias_id,
        "nome_categoria": nome
    }
    categorias.append(nova_categoria)
    salvar_arquivo(ARQUIVOS_CATEGORIAS, categorias)
    categorias_id+=1
