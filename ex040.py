"""Exercício Python 040: Crie um programa que leia duas notas de um aluno
e calcule a sua média, mostrando uma mensagem no final, conforme a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""

nota_1 = float(input('Digite a nota do primeiro semestre: '))
nota_2 = float(input('Digite a nota do segundo semestre: '))
media = (nota_1 + nota_2)/2
print('A média do aluno que tirou {:.2f} no primiero semestre e depois tirou {:.2f} no segundo semestre foi de {}'.format(nota_1, nota_2, media))
if media < 5:
    print('\033[4;31mO aluno foi REPROVADO, pois ficou abaixo da média de 5 pontos!')
    print('Média do aluno: {:.2f}'.format(media))
elif 5 <= media <= 6.9:
    print('\033[4;33mO aluno está em recuperação pois ficou com a média entre 5 e 6.9')
    print('Média do Aluno: {:.2f}'.format(media))
else:
    print('\033[4;32mO ALUNO FOI APROVADO! Ficou acima da média de 7 pontos!')
    print('Média do aluno: {:.2f}\nPARABÉNS!'.format(media))
