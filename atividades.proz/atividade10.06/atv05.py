'''
Exercício 5: Cálculo de Desconto
Peça ao usuário o valor de um produto e o percentual de desconto. Calcule e mostre o
valor com o desconto aplicado.
'''
produto = float(input('Qual o preço do produto? R$'))
percentual = float(input('Qual o percentual de desconto? %'))
print('O valor do produto {}R$, com desconto de {}% é de {}R$'.format(produto, percentual, produto - (produto*percentual/100)))