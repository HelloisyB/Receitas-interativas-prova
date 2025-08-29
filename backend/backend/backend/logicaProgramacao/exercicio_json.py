#criar cadastro de ususario
#o usuario deve ter os seguintes campos (nome, telefone, cidade, idade, e sexo)
#usar função try/execept e laços

import json

usuarios = []

try:
    with open('usuarios.json', 'r') as arquivo:
        usuarios = json.load(arquivo)
        print("Arquivo de usuários carregado.")
except FileNotFoundError:
    print("Arquivo não encontrado. Iniciando novo cadastro de usuários.")

print("\n--- Cadastro de Usuário ---")

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
cidade = input("Digite a cidade: ")

#idadr
while True:
    try:
        idade = int(input("Digite a idade: "))
        break
    except ValueError:
        print("Idade inválida. Digite apenas números inteiros.")

#genero
while True:
    sexo = input("Digite o sexo (M/F/Outro): ").strip().lower().upper()
    if sexo in ['M', 'F', 'Outro']:
        break
    
    else:
        print("Opção inválida. Digite M, F ou Outro.")

#menu usuário
novo_usuario = {
    "nome": nome,
    "telefone": telefone,
    "cidade": cidade,
    "idade": idade,
    "sexo": sexo
}

usuarios.append(novo_usuario)

with open('usuarios.json', 'w') as arquivo:
    json.dump(usuarios, arquivo, indent=4)

print(f"\nUsuário {nome} cadastrado com sucesso!")
