"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('JOGANDO PAR OU ÍMPAR COM O COMPUTADOR')
numero_de_vitórias = 0
while True:
    print('-'*50)
    escolha_do_pc = randint(0, 100)
    escolha_numerica_do_usuario = int(input('Digite um número: '))
    opção_do_usuário = str(input('Você quer ímpar ou par? ')).lower().strip()[0]
    while opção_do_usuário != 'p' and opção_do_usuário != 'i':
        print('OPÇÃO INVÁLIDA!')
        opção_do_usuário = str(input('Você quer ímpar ou par? ')).lower().strip()[0]
    if opção_do_usuário == 'p':
        soma_dos_valores = escolha_numerica_do_usuario + escolha_do_pc
        if soma_dos_valores % 2 == 0:
            print(f'O computador escolheu {escolha_do_pc} e você escolheu {escolha_numerica_do_usuario}.'
                  f'\nA soma das escolhas é igual a {soma_dos_valores} que é PAR!')
            print('\033[7;32mPARABÉNS! Você venceu o computador.\033[m')
            numero_de_vitórias += 1
            print('Vamos jogar novamente...')
        else:
            print(f'O computador escolheu {escolha_do_pc} e você escolheu {escolha_numerica_do_usuario}. A soma das escolhas é igual a {soma_dos_valores} que é ÍMPAR!')
            print('\033[7;31mVocê perdeu!\033[m')
            break
    elif opção_do_usuário == 'i':
        soma_dos_valores = escolha_numerica_do_usuario + escolha_do_pc
        if soma_dos_valores % 2 != 0:
            print(f'O computador escolheu {escolha_do_pc} e você escolheu {escolha_numerica_do_usuario}. A soma das escolhas é igual a {soma_dos_valores} que é PAR!')
            print('\033[7;32mPARABÉNS! Você venceu o computador.\033[m')
            numero_de_vitórias += 1
            print('Vamos jogar novamente...')
        else:
            print(f'O comuputador escolheu {escolha_do_pc} e você escolheu {escolha_numerica_do_usuario}. A soma das escolhas é igual a {soma_dos_valores} que é ÍMPAR!')
            print('\033[7;31mVocê perdeu!\033[m')
            break
print('-' * 50)
print('OBRIGADO POR TER JOGADO COMIGO!')
print(f'Você ganhou de mim {numero_de_vitórias} vezes')
