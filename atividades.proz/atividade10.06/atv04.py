'''
Peça ao usuário seu peso (em kg) e altura (em metros), e calcule o Índice de Massa
Corporal (IMC) utilizando a fórmula: IMC = peso / (altura * altura).
'''
peso = float(input('Qual é seu peso em Kg: '))
alt = float(input('Qual a altura: '))
print('O calculo do IMC, para uma pessoa que pesa {}Kg, e tem {} de altura é de {:.w}'.format(peso, alt, peso/(alt*alt)))