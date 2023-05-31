"""
Exercício Python 46: Faça um programa que mostre na tela
uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep
print('Contagem regressiva de 10 até 0 automática em python.\n')
for contagem_regressiva in range(10, -1, -1):
    print(contagem_regressiva)
    sleep(1)
print('\n{:*^20}'.format(' FIM DA CONTAGEM!'))
print('BOOOM! 💣')
'''
PEGANDO UM NÚMERO DIRETO DO USUÁRIO.

from time import sleep
print('\033[36m{:=^50}\033[m'.format(' Cronometro de Contagem Regressiva! '))
numero = int(input('Digite um valor: '))
for contagem_regressiva in range(numero, 0, -1):
    print(contagem_regressiva)
    sleep(1)
'''