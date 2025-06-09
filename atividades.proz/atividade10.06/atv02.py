'''
Exercício 2: Conversão de Temperatura
Peça uma temperatura em Celsius ao usuário e converta-a para Fahrenheit utilizando a
fórmula: Fahrenheit = (Celsius * 9/5) + 32.
'''
celsius = float(input('Qual a temperatura em celsius(°c)? '))
print('A temperatura em fahrenheit(°F) {}°F'.format(celsius*9/5 + 32))
