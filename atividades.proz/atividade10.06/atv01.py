'''
Exercício 1: Preço a pagar 
Crie um programa que cadastre o valor do café (um número) e pergunte para ele 
quantos cafés ele irá querer comprar e apresente o resultado a pagar. 
'''
valor_cafe = float(input("Qual é o valor do cafe? R$"))
quantidade_cafe = float(input('Qual a quantidade de cafe você deseja? '))
print("O valor do café é {} \nvocê pagará {}R$ por {}cafe(s)".format(valor_cafe, valor_cafe*quantidade_cafe, quantidade_cafe))