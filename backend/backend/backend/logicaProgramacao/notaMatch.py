nota = int(input("Digite a nota (0 a 10): "))
match nota:
    case 10:
        print("aprovado parabéns!")
    case 7 | 8 | 9:
        print("Aprovado.")
    case 0 | 1 | 2 | 3 | 4 | 5 | 6:
        print("Reprovado.")
    case _:
        print("Nota inválida.")
        
