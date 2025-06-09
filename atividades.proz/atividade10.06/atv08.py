'''
Exercício 8: Numeros negativos
Crie um programa utilizando um vetor de 4 posições onde o usuário irá digitar 4 números.
O programa irá retornar quantos números negativos foram digitados.
'''
# Cria um vetor vazio para armazenar os 4 números
vetor = []
negativos = 0

# Solicita 4 números ao usuário
for i in range(4):
    num = float(input(f"Digite o {i+1}º número: "))
    vetor.append(num)
    # Verifica se o número é negativo
    if num < 0:
        negativos += 1

# Exibe o vetor e a quantidade de números negativos
print(f"Vetor: {vetor}")
print(f"Quantidade de números negativos: {negativos}")