#lidar com erros de forma controlada.
# Em vez de o programa quebrar quando ocorre um erro, você pode "tentar" executar um bloco de código (try),
# e se ocorrer um erro, você pode "capturar" esse erro e tratar ele de alguma forma (except).

#---
try:
    # código que pode causar um erro
    resultado = 10 / 0
except:
    # código que será executado se houver um erro
    print("Ocorreu um erro!")

#---
#erros especificos
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Isso não é um número válido.")

#---
#else: executado somente se não houver erro
#finally: executado sempre, com ou sem erro (útil para liberar recursos, como arquivos abertos)
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Erro: valor inválido.")
else:
    print("Você digitou:", numero)
finally:
    print("Fim da tentativa.")