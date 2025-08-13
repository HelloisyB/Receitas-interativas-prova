#crie um arq. chamdo terceirão
#insira o nome dos alunos na lista
#encerre com a palavra "emcerrar"
#liste o nome de todos os alunos da seguinte forma - "aluno:" = nome
def cadastrar_alunos():
    print("Alunos do Terceirão")
    print("Digite 'encerrar' para finalizar a lista.")
    
    with open("terceirão.txt", "w") as arquivo:
        while True:
            nome = input("Digite o nome do aluno: ")
            if nome.lower() == "encerrar":
                print("Lista finalizada!")
                break
            arquivo.write(nome + "\n")

def listar_alunos():
    arquivo = open("terceirão.txt", "r")
    print("\n----- Alunos do Terceirão -----")
    for linha in arquivo:
        nome = linha.strip()
        if nome:
            print(f"aluno: {nome}")
    arquivo.close()

if __name__ == "__main__":
    cadastrar_alunos()
    listar_alunos()
