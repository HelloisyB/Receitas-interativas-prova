#open("arquivo.txt", modo)
#modo de leitura__"R"
#modo de escrita__"W"__substitui o conteúdo
#modo de escrita__"A"__acresta o conteúdo

#open("arquivo.txt",'w')/as arquivo
#arquivo.write("hello word")
#arquivo.write("tudo bem?")

#conteudo=arquivo.read()
#print(conteudo)

#strip remove os espaços

def gerar_lista_compras():
    print("Seja bem-vindo")
    print("Para encerrar, digite 'fim'.")
    
    with open("comida.txt", 'w') as comida:
        while True:
            item = input("Digite o item: ")
            if item.lower() == "fim":
                print("Encerrando lista.")
                break
            comida.write(item + "\n")
gerar_lista_compras()

def lista_itens():
    with open("comida.txt", 'r') as comida:
        print("----Lista de compras----")
        for item in comida:
            produto = item.strip()
            print("item:", produto)

lista_itens()
