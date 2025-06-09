'''
Exercício 6: Calculadora de Juros Simples
Solicite ao usuário um valor principal, a taxa de juros (em porcentagem) e o número de
anos. Calcule o montante final utilizando a fórmula: Montante = principal + (principal * taxa
de juros * anos / 100).
'''
valor_principal = float(input('Qual o valor para o cálculo: '))
taxa = float(input('Qual o valor da taxa para o cálculo: '))
ano = float(input('Qual a quantidade de anos para o cálculo: '))
print('O montante final, para o valor de {}R$, com a taxa de {}%, no período de {}anos é de {}'.format(valor_principal, taxa, ano, valor_principal + (valor_principal*taxa*ano/100)))