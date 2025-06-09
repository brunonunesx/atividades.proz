'''
Exercício 11: Classificação de Triângulos
Peça ao usuário os comprimentos dos três lados de um triângulo e determine se é
equilátero, isósceles ou escaleno.
'''
# Solicita os comprimentos dos três lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se os lados formam um triângulo válido
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os comprimentos fornecidos não formam um triângulo válido.")