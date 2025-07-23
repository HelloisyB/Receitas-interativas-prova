#laço para contar ate 10
def contar_ate_dez():
    for i in range(1, 11): #intervalo
        print(i)
contar_ate_dez()

#receber mome e numero, imprimir o nome na tela a quantidade de vezes indicadas
nome = input("digite o nome:")
quantidade = int(input("digite a quantidade desejada:"))
for i in range(quantidade):
    print(nome)

#cinco numeros e some todos eles usando o laço
soma = 0
for i in range(5):
  numero = float(input(f"digite o numero {i+1}: "))
  numero = float(input("digite o numero" + (i+1) + ":")) #professor
  soma += numero
  print(f"a soma dos cinco numeros é: {soma}")

# Receber número e imprimir tabuada de 1 a 10
numero = int(input("Digite um número: "))
print("Tabuada do:", numero)
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}") 
    
# Mostrar números pares entre 1 e 20
print("Números pares entre 1 e 20:")
for i in range(1, 21):  # De 1 a 20
    if i % 2 == 0:  # Verifica se o número é par
        print(i)