"""
Exercício Python 51: Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

print('{:*^41}'.format(' Calculando a progressão aritimética '))
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão dessa progressão aritimética: '))
for progressao_aritimetica in range(primeiro_termo, primeiro_termo + 10 * razao, razao):
    print('\033[1;36m{} → '.format(progressao_aritimetica), end='')
print('ACABOU!')
