"""
Exercício Python 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números gerados pelo computador foram: {tupla}')
print(f'O maior número dessa tupla é {max(tupla)}!')
print(f'O menor número dessa tupla é {min(tupla)}!')
