'''
Exercício 10: Verificação de Número Positivo, Negativo ou Zero
Solicite um número e determine se é positivo, negativo ou zero.
'''
# Solicita um número do usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")