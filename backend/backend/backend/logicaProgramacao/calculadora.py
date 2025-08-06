num1 = int(input("Digite o numero:"))
num2 = int(input("Digite o numero:"))
operação = input("Digite a operação (+, -, * ou /): ")

match operação:
    case "+":
        soma = num1 + num2
        print("A soma é igual a:", soma)
    case "-":
        subtracao = num1 - num2
        print("A subtração é igual a:", subtracao)
    case "*":
        multiplicacao = num1 * num2
        print("A multiplicação é igual a:", multiplicacao)
    case "/":
        divisao = num1/num2
        print("a divisão é igual a:", divisao)
