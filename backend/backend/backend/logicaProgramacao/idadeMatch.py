idade = int(input("Digite sua idade: "))

match idade:
    case x if x < 12:
        print("Você é uma criança.")

    case x if x > 12 and x < 18:
        print("Você é um adolescente.")

    case x if x >= 18 and x < 60:
        print("Você é um adulto.")

    case x if x >= 60 and x < 100:
        print("Você é um idoso.")

    case x if x >= 100:
        print("Você é uma múmia!")
