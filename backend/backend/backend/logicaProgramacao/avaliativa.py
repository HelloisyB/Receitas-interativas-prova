#exercicip 1
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#exercicio 2
numero = int(input("Digite um número inteiro: ")) 

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#Exercício 3
for numero in range(10, 0, -1):  
    print(numero) 

# atv 4
numero = int(input("Digite um número: "))

for i in range(1, 11):  
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#5
soma_total = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    soma_total += numero 

print(f"A soma total dos números digitados é: {soma_total}")

#6
numero_secreto = 9
tentativa = None 

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinhar o número secreto: ")) 
    
    if tentativa < numero_secreto:
        print("Muito baixo! Tente novamente.") 
    elif tentativa > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns, você acertou!")

#seteeeeeeeeeee
lista_compras = ["maracuja", "chocolate", "suco"]

print("\nLista Inicial:")
print(*[f"{i+1}. {item}" for i, item in enumerate(lista_compras)], sep="\n")

while True:
    novo_item = input("\nNovo item (ou 'sair' para encerrar): ").strip()
    
    if novo_item.lower() == 'sair':
        break
        
    if novo_item:
        lista_compras.append(novo_item)
        print("\nLista Atualizada:")
        print(*[f"{i+1}. {item}" for i, item in enumerate(lista_compras)], sep="\n")
    else:
        print("Por favor, digite um item")

print("\nLista Final:", lista_compras)

#8
numeros = [9, 19, 99, 59, 89]
maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número na lista é: {maior_numero}")      