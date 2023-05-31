"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
Mostrando uma mensagem na tela:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))

if numero_1 > numero_2:
    print('O primeiro valor é o maior!')
    print('{} > {}.'.format(numero_1, numero_2))
elif numero_2 > numero_1:
    print('O segundo valor é o maior!')
    print('{} > {}.'.format(numero_2, numero_1))
else:
    print('Não existe um valor maior. Os dois números digitados são iguais.')
    print('{} = {}.'.format(numero_1, numero_2))
