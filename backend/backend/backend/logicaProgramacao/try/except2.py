#criar um cadastro de usuario com arquivos (função e try/excety)
#criar a listagem desses usuarios
##alterar um usuario cadastrado (no arquivo)
#excluir usuario cadastrado

def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ").strip()  #pede o nome e remove espaços extras
        with open("usuarios.txt", "a") as arquivo:  #abre o arquivo no modo de adicionar ("append")
            arquivo.write(nome + "\n")  #escreve o nome no arquivo, com quebra de linha
        print("Usuário cadastrado com sucesso.")
    except Exception as erro:
        print("Erro ao cadastrar:", erro)

def listar_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo no modo leitura ("read")
            linhas = arquivo.readlines()  #lê todas as linhas do arquivo e guarda numa lista chamada 'linhas'
            # Ex: ['Maria\n', 'João\n']

            if not linhas:  #se a lista estiver vazia, ou seja, sem usuários
                print("Nenhum usuário encontrado no cadastro.")
            else:
                print("Usuários cadastrados:")
                for linha in linhas:
                    print("- " + linha.strip())  #strip() remove o '\n' do final da linha
    except FileNotFoundError:
        print("Arquivo não encontrado.")  #se o arquivo ainda não existir
    except Exception as erro:
        print("Erro ao listar usuários:", erro)

def alterar_usuario():
    try:
        nome_anterior = input("Digite o nome que deseja alterar: ").strip()

        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()  #Lê todas as linhas do arquivo

        usuario_encontrado = False
        novo_conteudo = []  #guardar os nomes atualizados

        for linha in linhas:
            nome = linha.strip()  #Remove o '\n' e espaços
            if nome == nome_anterior:
                novo_nome = input("Digite o novo nome: ").strip()
                novo_conteudo.append(novo_nome + "\n")  #para substituir o nome antigo
                usuario_encontrado = True
            else:
                novo_conteudo.append(linha)  #nome original

        if usuario_encontrado:
            with open("usuarios.txt", "w") as arquivo:  #abre o arquivo para sobrescrever (modo "write")
                arquivo.writelines(novo_conteudo)  #escreve todos os nomes novamente
            print("Usuário alterado com sucesso.")
        else:
            print("Usuário não encontrado.")
    except Exception as erro:
        print("Erro ao alterar usuário:", erro)

def excluir_usuario():
    try:
        nome_excluir = input("Digite o nome do usuário que deseja excluir: ").strip()

        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()  #para ler todas as linhas do arquivo

        novo_conteudo = []  #armazenar os nomes que ficarão
        usuario_encontrado = False

        for linha in linhas:
            #strip() remove espaços e \n do final
            #Se o nome da linha for diferente do nome que queremos excluir,
            #ele será mantido na lista novo_conteudo
            if linha.strip() != nome_excluir:
                novo_conteudo.append(linha)
            else:
                usuario_encontrado = True

        if usuario_encontrado:
            with open("usuarios.txt", "w") as arquivo:
                arquivo.writelines(novo_conteudo)  
            print("Usuário excluído com sucesso.")
        else:
            print("Usuário não encontrado.")
    except Exception as erro:
        print("Erro ao excluir o usuário:", erro)

# Função para cadastrar um usuário
def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ").strip()
        if nome:
            with open("usuarios.txt", "a") as arquivo:  # "a" = append (adicionar no final)
                arquivo.write(nome + "\n")
            print("Usuário cadastrado com sucesso.")
        else:
            print("Nenhum nome informado.")
    except Exception as erro:
        print("Erro ao cadastrar usuário:", erro)

# Função para listar usuários cadastrados
def listar_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas e guarda numa lista
            if not linhas:
                print("Nenhum usuário cadastrado.")
            else:
                print("Usuários cadastrados:")
                for linha in linhas:
                    print("- " + linha.strip())  # strip() tira o \n
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
    except Exception as erro:
        print("Erro ao listar usuários:", erro)

# Função para alterar um usuário existente
def alterar_usuario():
    try:
        nome_antigo = input("Digite o nome do usuário que deseja alterar: ").strip()
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        usuario_encontrado = False
        novo_conteudo = []

        for linha in linhas:
            nome = linha.strip()
            if nome == nome_antigo:
                novo_nome = input("Digite o novo nome: ").strip()
                novo_conteudo.append(novo_nome + "\n")
                usuario_encontrado = True
            else:
                novo_conteudo.append(linha)

        if usuario_encontrado:
            with open("usuarios.txt", "w") as arquivo:
                arquivo.writelines(novo_conteudo)
            print("Usuário alterado com sucesso.")
        else:
            print("Usuário não encontrado.")
    except Exception as erro:
        print("Erro ao alterar usuário:", erro)

# Função para excluir um usuário
def excluir_usuario():
    try:
        nome_excluir = input("Digite o nome do usuário que deseja excluir: ").strip()
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        novo_conteudo = []
        usuario_encontrado = False

        for linha in linhas:
            if linha.strip() != nome_excluir:
                novo_conteudo.append(linha)
            else:
                usuario_encontrado = True

        if usuario_encontrado:
            with open("usuarios.txt", "w") as arquivo:
                arquivo.writelines(novo_conteudo)
            print("Usuário excluído com sucesso.")
        else:
            print("Usuário não encontrado.")
    except Exception as erro:
        print("Erro ao excluir usuário:", erro)

# Menu principal
def menu():
    while True:
        print("\n====== MENU ======")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Alterar usuário")
        print("4. Excluir usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção de 1 a 5: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            alterar_usuario()
        elif opcao == "4":
            excluir_usuario()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
# Função para cadastrar um usuário
def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ").strip()
        if nome:
            with open("usuarios.txt", "a") as arquivo:  # "a" = append (adicionar no final)
                arquivo.write(nome + "\n")
            print("Usuário cadastrado com sucesso.")
        else:
            print("Nenhum nome informado.")
    except Exception as erro:
        print("Erro ao cadastrar usuário:", erro)

# Função para listar usuários cadastrados
def listar_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas e guarda numa lista
            if not linhas:
                print("Nenhum usuário cadastrado.")
            else:
                print("Usuários cadastrados:")
                for linha in linhas:
                    print("- " + linha.strip())  # strip() tira o \n
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
    except Exception as erro:
        print("Erro ao listar usuários:", erro)

# Função para alterar um usuário existente
def alterar_usuario():
    try:
        nome_antigo = input("Digite o nome do usuário que deseja alterar: ").strip()
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        usuario_encontrado = False
        novo_conteudo = []

        for linha in linhas:
            nome = linha.strip()
            if nome == nome_antigo:
                novo_nome = input("Digite o novo nome: ").strip()
                novo_conteudo.append(novo_nome + "\n")
                usuario_encontrado = True
            else:
                novo_conteudo.append(linha)

        if usuario_encontrado:
            with open("usuarios.txt", "w") as arquivo:
                arquivo.writelines(novo_conteudo)
            print("Usuário alterado com sucesso.")
        else:
            print("Usuário não encontrado.")
    except Exception as erro:
        print("Erro ao alterar usuário:", erro)

# Função para excluir um usuário
def excluir_usuario():
    try:
        nome_excluir = input("Digite o nome do usuário que deseja excluir: ").strip()
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        novo_conteudo = []
        usuario_encontrado = False

        for linha in linhas:
            if linha.strip() != nome_excluir:
                novo_conteudo.append(linha)
            else:
                usuario_encontrado = True

        if usuario_encontrado:
            with open("usuarios.txt", "w") as arquivo:
                arquivo.writelines(novo_conteudo)
            print("Usuário excluído com sucesso.")
        else:
            print("Usuário não encontrado.")
    except Exception as erro:
        print("Erro ao excluir usuário:", erro)

# Menu principal
def menu():
    while True:
        print("\n====== MENU ======")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Alterar usuário")
        print("4. Excluir usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção de 1 a 5: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            alterar_usuario()
        elif opcao == "4":
            excluir_usuario()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
menu()

