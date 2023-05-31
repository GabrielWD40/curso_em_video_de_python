""""
Esse algoritmo deve ler o nome completo de uma pessoa.
Depois, ele deverá mostrar qual é o primeiro e último nome dela.
"""

nome_completo = str(input('Digite o seu nome completo: ').title().strip())
nome_fatiado = nome_completo.split()

print('seu primeiro nome é: {}'.format(nome_fatiado[0]))
print('Seu último nome é: {}'.format(nome_fatiado[-1]))

"""
#outra maneira de fazer para pegar o último nome:
print('Seu último nome é: {}'.format(nome_fatiado[-1]))
"""
