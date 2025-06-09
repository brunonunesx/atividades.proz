'''
Exercício 14: Verificação de Vogal ou Consoante
Solicite ao usuário para digitar uma letra e determine se é uma vogal ou uma consoante.
'''
# Solicita uma letra do usuário
letra = input("Digite uma letra: ").lower()

# Verifica se a entrada é uma única letra válida
if len(letra) == 1 and letra.isalpha():
    # Verifica se a letra é uma vogal
    if letra in 'aeiou':
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")
else:
    print("Por favor, digite apenas uma letra válida.")