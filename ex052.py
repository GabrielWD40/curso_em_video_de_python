"""
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

numero_de_divisores = 0

print('{:=^50}'.format(' Verificando se um  número é primo! '))
numero = int(input('Digite um número inteiro qualquer: '))
for intervalo_de_numeros in range(1, numero+1):
    if numero % intervalo_de_numeros == 0:
        print('\033[32m{}'.format(intervalo_de_numeros), end=' \033[32m')
        #coloquei em verde os números que conseguem dividir o número em questão.
        numero_de_divisores = numero_de_divisores +1
    else:
        print('\033[31m{}'.format(intervalo_de_numeros), end=' \033[31m')
print('\n\033[mO número {} tem {} divisores.'.format(numero, numero_de_divisores))
if numero_de_divisores > 2:
    print('O número {} NÃO É PRIMO!'.format(numero))
else:
    print('O número {} É PRIMO!'.format(numero))

