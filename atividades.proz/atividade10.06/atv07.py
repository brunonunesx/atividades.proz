'''
Exercício 7: Troca de Valores
Solicite ao usuário dois valores e troque o valor da primeira variável com o da segunda
variável, e vice- versa.
'''
# Solicita dois valores do usuário
valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")

# Exibe os valores antes da troca
print(f"Antes da troca: valor1 = {valor1}, valor2 = {valor2}")

# Realiza a troca diretamente
valor1, valor2 = valor2, valor1

# Exibe os valores após a troca
print(f"Depois da troca: valor1 = {valor1}, valor2 = {valor2}")