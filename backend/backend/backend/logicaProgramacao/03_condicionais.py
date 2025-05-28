nome = input("Digite seu nome:")
print("Olá", nome)

valor1= int(input("Digite o primeiro valor"))
valor2= int(input("Digite o segundo valor"))

if(valor1 > valor2):
    print("O valor1 é maior que o valor2")

elif(valor2 > valor1):
    print("O valor2 é maior que o valor1")

else:
    print("Os valores são iguais")


nota1 = int(input("nota 1:"))
nota2 = int(input("nota 2:"))
nota3 = int(input("nota 3:"))
nota4 = int(input("nota 4:"))
media = (nota1 + nota2 + nota3 + nota4) /4

if (media == 100):
    print("Exelente", media)
elif (media >= 80 and media <= 99):
    print("Muito bom.", media)
elif(media >= 70 and media<= 79):
    print("Na raspa.", media)
elif(media > 70):
    print("Precisa melhorar", media)
else:
    print("valores invalidos", media)
