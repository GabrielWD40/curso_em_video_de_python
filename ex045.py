"Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."
# atribuir valores

from random import choice
from time import sleep

print('\033[33m{:*^40}\033[m'.format(' Jogando Jokenpô com o computador '))
# lembre-se que para usar o centralizador, vc tem que colocar os dois pontos dentro das chaves {:}.
print('Escolha das uma opção abaixo:')
print('[ 1 ] - PEDRA\n[ 2 ] - PAPEL\n[ 3 ] - TESOURA')
escolha_do_usuario = int(input('Escolha o número de das opções acima: ').strip())
escolha_do_pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
sleep(1)
print('\033[33mJO ', end='')
sleep(1)
print('KEN ', end='')
sleep(1)
print('PÔ!\033[m')
# esse efeito que fiz da animação de jokenpô.

# Aqui o pc faz uma condição aninhada se você escolher a opção 1 - PEDRA

if escolha_do_usuario not in [1, 2, 3]:
    print('DIGITE UMA OPÇÃO VÁLIDA!')
    sleep(1)
    print('\033[1;36mBO - ', end='')
    sleep(1)
    print('BÃO')
    sleep(1)
elif escolha_do_usuario == 1:
    print('Você escolheu PEDRA!')
    print('O computador escolheu {}!'.format(escolha_do_pc.upper()))
    if escolha_do_pc == 'PEDRA':
        print('\n🗿 vs 🗿')
        print('\033[33mDEU EMPATE!\033[m')
    elif escolha_do_pc == 'TESOURA':
        print('\n🗿 vs ✂ ')
        print('\033[1;32mVOCÊ GANHOU DO COMPUTADOR!')
    else:
        print('\n🗿 vs 📜')
        print('\033[1;31mVOCÊ PERDEU!')
# Fim da opção 1.

# Aqui o pc faz uma condição aninhada se você escolher a opção 2 - PAPEL
elif escolha_do_usuario == 2:
    print('Você escolheu PAPEL!')
    print('O computador escolheu {}!'.format(escolha_do_pc.upper()))
    if escolha_do_pc == 'PEDRA':
        print('\n📜 vs 🗿')
        print('\033[1;32mVOCÊ GANHOU COM COMPUTADOR!\033[m')
    elif escolha_do_pc == 'TESOURA':
        print('\n📜 vs ✂️')
        print('\033[1;31mVOCÊ PERDEU!')
    else:
        print('📜 vs 📜')
        print('\033[1;33mDEU EMPATE!')
# Fim da opção 2.

# Aqui o pc faz uma condição aninhada se você escolher a opção 3 - TESOURA
elif escolha_do_usuario == 3:
    print('Você escolheu TESOURA!')
    print('O computador escolheu {}'.format(escolha_do_pc.upper()))
    if escolha_do_pc == 'PEDRA':
        print('✂️ vs 🗿')
        print('\033[1;31mVOCÊ PERDEU!')
    elif escolha_do_pc == 'PAPEL':
        print('✂️ vs 📜')
        print('\033[32mVOCÊ GANHOU!')
    else:
        print('✂️ vs ✂️')
        print('\033[1;33mDEU EMPATE!')
# Fim da opção 3.

# Aqui o pc faz uma condição aninhada se você escolher uma coisa aleatória.

"""
=========================================================================
opcoes_permitidas = [1, 2, 3]
escolha_do_usuario = int(input('Escolha uma opção: '))

if escolha_do_usuario not in opcoes_permitidas:
    print('Opção inválida. Escolha uma opção entre', opcoes_permitidas)
=========================================================================

Nesse exemplo, o programa verifica se a escolha do usuário não está na lista opcoes_permitidas. Se a escolha for inválida, o programa exibe uma mensagem de erro.
"""
