'''
Exercício 13: Verificação de Número Divisível por 3 e 5
Peça ao usuário para digitar um número e verifique se é divisível por 3 e 5 ao mesmo
tempo.
'''
# Solicita um número do usuário
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 3 e 5 ao mesmo tempo
if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e 5 ao mesmo tempo.")
else:
    print("O número não é divisível por 3 e 5 ao mesmo tempo.")