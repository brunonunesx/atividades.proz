'''
Exercício 12: Aprovação em Disciplina
Solicite a nota do aluno em uma disciplina e determine se ele foi aprovado (nota maior ou
igual a 7) ou reprovado.
'''
# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Verifica se o aluno foi aprovado ou reprovado
if nota >= 7:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")