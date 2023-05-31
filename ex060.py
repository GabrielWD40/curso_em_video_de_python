"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""
# Forma fácil de resolver em python:
from math import factorial
from time import sleep
numero = int(input('Digite um número: '))
fatorial = factorial(numero)
print('O fatorial de {} é = {}!'.format(numero, fatorial))
print()
sleep(0.5)
print()
# Maneira mais complexa:
numero = int(input('Digite um número: '))
contador = numero  # O contador servirá para conseguirmos fazer o fatorial funcionar, diminuindo 1 consecutivamente.
fatorial = 1  # Segundo o professor Guanabara, para obetermos uma multiplicação sucessiva limpa, inicie uma variável com o valor 1.

while contador > 0:  # Enquanto contador foir maio que 0 faça:
    print('{}'.format(contador), end='')  # Imprime o valor atual do contador/renovado depois da estrutura de repetição e o que vem depois fica na mesma linha
    print(' x ' if contador > 1 else ' = ', end='')  # Ele imprime " x " se o valor do contador for maior que 1, se não ele usa o '='.
    fatorial *= contador
    contador -= 1
print(fatorial)
