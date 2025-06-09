'''
Exercício 15: Cálculo de Desconto com Condição
Peça ao usuário o valor de um produto e calcule o valor com desconto apenas se o valor
original for maior que R$ 100.
'''
# Solicita o valor do produto
valor_original = float(input("Digite o valor do produto (em R$): "))

# Define a taxa de desconto (por exemplo, 10%)
desconto = 0.10  # 10%

# Verifica se o valor original é maior que R$ 100
if valor_original > 100:
    valor_desconto = valor_original * desconto
    valor_final = valor_original - valor_desconto
    print(f"O valor original é R$ {valor_original:.2f}.")
    print(f"Desconto de {desconto*100:.0f}% aplicado: R$ {valor_desconto:.2f}.")
    print(f"Valor final com desconto: R$ {valor_final:.2f}.")
else:
    print(f"O valor original é R$ {valor_original:.2f}.")
    print("Nenhum desconto aplicado, pois o valor é menor ou igual a R$ 100.")