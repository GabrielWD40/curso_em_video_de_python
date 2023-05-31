"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
import time
from math import fsum

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))
escolha = None
while escolha != '5':
    print('\033[36m=-=\033[m'*20)
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    escolha = str(input('Escolha uma das opções: '))
    if escolha == '1':
        print()
        print('A soma entre {:.1f} + {:.1f} = {:.1f}'.format(primeiro_numero, segundo_numero, primeiro_numero + segundo_numero))
    elif escolha == '2':
        print()
        print('Multiplicação: {:.1f} x {:.1f} = {:.1f}'.format(primeiro_numero, segundo_numero, primeiro_numero * segundo_numero))
    elif escolha == '3':
        print()
        if primeiro_numero > segundo_numero:
            print('O {} é maior que {}.'.format(primeiro_numero, segundo_numero))
        elif primeiro_numero == segundo_numero:
            print('Os dois números são iguais.')
        else:
            print('O {} é maior que {}'.format(segundo_numero, primeiro_numero))
    elif escolha == '4':
        primeiro_numero = float(input('Digite o novo valor do primeiro número: '))
        segundo_numero = float(input('Digite o novo valor do segundo número: '))
    elif escolha == '5':
        print('Finzalizando...')
        time.sleep(1)
    else:
        print('\033[31mOPÇÃO INVÁLIDA! Por favor, digite o número de uma das opções acima.\033[m')
    print('\033[36m=-=\033[m'*20)
    print()
print('OBRIGADO POR USAR OS SISTEMAS!')
