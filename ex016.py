#esse var=Noneo deve mostrar somente a parte interia de um número com casas decimais.
from math import trunc
#import math (importa toda a biblioteca de matemática)
numero = float(input('Digite um número com vírgula qualquer: '))

print('O número digitado foi {} \ne a sua parte inteira é = {}'.format(numero, trunc(numero)))
''' 
A função trunc é aquela que ignora as casas decimais e só mostra o número inteiro.

O outro método é:
numero = float(input('Digite um número com vírgula qualquer: '))

print('O número digitado foi {} \ne a sua parte inteira é = {}'.format(numero, int(numero)))
'''