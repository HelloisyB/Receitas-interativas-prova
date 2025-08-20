# Nome do arquivo onde as palavras serão salvas
arquivo_palavras = "palavras.txt"

# Parte 1: Cadastro das palavras
with open(arquivo_palavras, "w") as arquivo:
    print("Cadastro de palavras. Digite 'sair' para encerrar.")
    while True:
        palavra = input("Digite uma palavra: ").strip()
        if palavra.lower() == "sair":
            break
        arquivo.write(palavra + "\n")

# Parte 2: Jogo de adivinhação
# Lê as palavras do arquivo
with open(arquivo_palavras, "r") as arquivo:
    lista_palavras = [linha.strip().lower() for linha in arquivo]

# Início do jogo
print("\nJogo de adivinhação! Tente adivinhar uma palavra cadastrada.")

while True:
    tentativa = input("Digite sua tentativa (ou 'sair' para encerrar): ").strip().lower()
    if tentativa == "sair":
        print("Jogo encerrado.")
        break
    if tentativa in lista_palavras:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Tente novamente.")
