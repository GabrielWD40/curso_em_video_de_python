"""
Esse algoritmo deve informar se o número digitado é par ou ímpar.
"""
print('Vamos verificar se seu número é PAR OU ÍMPAR')
numero = int(input('Digite um número inteiro qualquer: '))
if numero%2 == 0:
    print('O NÚMERO {} É PAR!'.format(numero))
else:
    print('O NÚMERO {} É ÍMPAR'.format(numero))