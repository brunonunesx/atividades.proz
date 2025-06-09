'''
Exercício 16: Classificação de Idade
Solicite a idade do usuário e classifique-a em "Criança", "Adolescente", "Adulto Jovem" ou
"Adulto".
'''
# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se a idade é válida (não negativa)
if idade >= 0:
    # Classifica a idade
    if idade <= 12:
        print("Você é uma Criança.")
    elif idade <= 17:
        print("Você é um Adolescente.")
    elif idade <= 24:
        print("Você é um Adulto Jovem.")
    else:
        print("Você é um Adulto.")
else:
    print("Por favor, digite uma idade válida (não negativa).")