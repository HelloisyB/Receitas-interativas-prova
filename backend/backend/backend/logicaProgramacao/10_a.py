#pedir ao usuario um valor - verdadeiro, somar valor total. falso, subtrair valor total.
#soma total de valores e mostrar na tela
#ao digitar zero, encerre o programa e mostre a soma uma ultima vez

total = 0

# Inicia um loop infinito
while True:
    valor = float(input("Digite um valor: "))
    
# Se o valor digitado for 0, sai do laçp
    if valor == 0:
        break
        
    operacao = input("Operação: [V]erdadeiro/Somar ou [F]also/Subtrair? ").upper() #.upper() é um método de strings que converte todos os caracteres de uma string para letras maiúsculas
    
    if operacao == 'V':
        total += valor
        print(f"+ {valor}")
    elif operacao == 'F':
        total -= valor
        print(f"- {valor}")
    else:
        print("Operação inválida! Use V ou F.")
print(f"\nTotal final: {total}")