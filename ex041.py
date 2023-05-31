"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""
from datetime import date
print('Olá! Vamos classificar a categoria do seu atleta.')
ano_de_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
categoria_do_atleta = ano_atual - ano_de_nascimento

if categoria_do_atleta <= 9:
    print('considerando o ano atual ({}), seu atleta tem {} anos.'.format(ano_atual, ano_atual - ano_de_nascimento))
    print('Esse atleta é da categoria MIRIM!')
elif 9 < categoria_do_atleta <= 14:
    print('Considerando o ano atual ({}), seu atleta tem {} anos.'.format(ano_atual, ano_atual - ano_de_nascimento))
    print('Esse atleta está na categoria INFANTIL!')
elif 14 < categoria_do_atleta <= 19:
    print('Considerando o ano atual ({}), seu atleta tem {} anos.'.format(ano_atual, ano_atual - ano_de_nascimento))
    print('Esse atleta está na categoria JÚNIOR!')
elif 19 < categoria_do_atleta <=25:
    print('Considerando o ano atual ({}), seu atleta tem {} anos.'.format(ano_atual, ano_atual - ano_de_nascimento))
    print('Essa atleta está na categoria SÊNIOR!')
else:
    print('Considerando o ano atual ({}), seu atleta tem {} anos.'.format(ano_atual, ano_atual - ano_de_nascimento))
    print('Esse atleta está na categoria MASTER!')
