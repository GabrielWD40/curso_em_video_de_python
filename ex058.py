"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.

"""
from random import randint
from time import sleep
print('JOGO DE ADIVINHAÇÃO! O PC escolhe um número e você precisa advinhar qual é.')
escolha_do_pc = randint(1, 10)
escolha_do_usuario = int(input('Digite um número: '))
numero_de_tentativas = 1
while escolha_do_usuario != escolha_do_pc:
    numero_de_tentativas += 1
    if escolha_do_usuario > escolha_do_pc:
        print('\033[4;31mVocê errou!\033[mO valor é menor que esse.')
        escolha_do_usuario = int(input('Digite um número: '))
    else:
        print('\033[1;31mVocê errou!\033[mO valor é mais baixo.')
        escolha_do_usuario = int(input('Digite um número: '))
print('\033[4;32mVOCÊ ACERTOU!!\033[m')
print('O número escolhido pelo PC é o {}, o mesmo que tu chutou({}).'.format(escolha_do_pc, escolha_do_usuario))
print('Depois de {} tentativas, você acertou!'.format(numero_de_tentativas))
