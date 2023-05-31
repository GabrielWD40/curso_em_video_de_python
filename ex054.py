"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
total_jovens = 0
total_adultos = 0
ano_atual = date.today().year
for verificador in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(verificador)))
    if ano_atual - ano >= 21:
        total_adultos += 1
    elif 0 < ano_atual - ano < 21:
        total_jovens += 1
print('Com base no que você informou e no ano atual ({}):'
      '\nHá {} pessoas maiores de idade.(maiores de 21 anos)'
      '\nHá {} pessoas menores de idade.(menores de 21 anos)'.format(ano_atual, total_adultos, total_jovens))
