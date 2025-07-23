#pedir que o usuario informe o salario
#calcular o salario anual

#se o salario for maior que R$5.000, calcular imposto de 12% e mostar o resultado
#for de R$2000 a R$4999, 7%
#for menor que R$2000, 3%

#informar
salario_mensal = float(input("Seu salario mensal é: R$"))

#calcular salario do ano
salario_anual = salario_mensal * 12

print(f"seu salario anual é:R${salario_anual}")

#IMPOSTOO
if(salario_mensal >= 5000):
    imposto = salario_mensal * 0.12
    print("seu imposto é: ", imposto)


elif(salario_anual >= 2000):
    imposto = salario_anual * 0.07
    print("imposto é:", imposto)

else:
    imposto = salario * 0.03
    print("seu imposto é:", imposto) 

# Mostrar salário líquido anual
salario_liquido = salario_anual - imposto
print(f"Seu salário líquido anual é: R$ {salario_anual}")

#infernooo
