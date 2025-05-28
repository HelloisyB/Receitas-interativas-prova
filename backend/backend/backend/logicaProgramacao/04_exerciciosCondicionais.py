idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você ainda não pode votar.")

# segundo exercicio 
    
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# terciero exercicios
    
numero1 = int(input("Escreva um numero:"))
numero2 = int(input("Escreva um numero:"))

if numero > numero2:
    print("O primeiro é maior.")
elif numero2 > numero1: 
    print("O segundo é menor.")
else:
    print("Os numeros são iguais.")    