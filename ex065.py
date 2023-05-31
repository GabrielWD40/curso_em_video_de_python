"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
print('\033[33m=\033[m'*70)
print('Digite números aleatóriamente!'
      '\n→ Vamos te dizer qual o maior número digitado.'
      '\n→ Vamos te dizer qual o menor número digitado'
      '\n→ Vamos te dizer qual a média dos números digitados.\n')
numero = float(input('Digite um número: '))
maior_numero = menor_numero = 0
soma_dos_numeros_digitados = numero
total_de_numeros_digitados = 1
escolha = str(input('Você deseja continuar?(sim / não) ')).strip().lower()

while escolha[0] != 'n':
    while escolha[0] != 's' and escolha[0] != 'n':
        print('\033[1;31m\nOPÇÃO INVÁLIDA!!\033[m')
        escolha = str(input('Por favor, digite uma opção válida (sim/não): '))
    while escolha[0] == 's':
        numero = float(input('\nDigite outro número: '))
        soma_dos_numeros_digitados += numero
        total_de_numeros_digitados += 1
        if total_de_numeros_digitados == 2:
            maior_numero = menor_numero = numero
        else:
            if numero > maior_numero:
                maior_numero = numero
            if numero < menor_numero:
                menor_numero = numero
        escolha = str(input('Você deseja continuar?(sim / não) ')).strip().lower()
if total_de_numeros_digitados == 1:
    maior_numero = numero
    menor_numero = numero
print('\033[33m=\033[m'*70)
print('A média dos {} números digitados é = \033[4;33m{:.2f}\033[m'.format(total_de_numeros_digitados, soma_dos_numeros_digitados / total_de_numeros_digitados))
print('O maior número digitado foi \033[4;33m{}\033[m'.format(maior_numero))
print('O menor número digitado foi \033[4;33m{}\033[m'.format(menor_numero))
print('\033[33m=\033[m'*70)
