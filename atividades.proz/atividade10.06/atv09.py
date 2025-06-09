'''
Exercício 9: Verificação de Idade para Dirigir
Peça a idade do usuário e verifique se ele tem idade suficiente para dirigir (idade mínima
de 18 anos).
'''
# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se a idade é suficiente para dirigir
if idade >= 18:
    print("Você tem idade suficiente para dirigir!")
else:
    print("Você não tem idade suficiente para dirigir. A idade mínima é 18 anos.")