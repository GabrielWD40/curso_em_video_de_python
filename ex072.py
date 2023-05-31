"""
Exercício Python 72:
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', "quinze", 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeros_por_algarismos = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
escolha = None
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('OPÇÃO INVÁLIDA!\nDigite um número entre 0 20: '))
    nome_do_numero_digitado = numeros_por_algarismos.index(numero)
    print(f'você digitou o número {numero} =[{numeros_por_extenso[nome_do_numero_digitado]}]!')
    print()
    escolha = str(input('Deseja continuar? [Sim / Não]: ')).strip().lower()
    while escolha[0] not in 'ns':
        escolha = str(input('OPÇÃO INVÁLIDA! Deseja continuar? [Sim / Não]: '))
    if escolha[0] == 'n':
        break

'''
# SOLUÇÃO DO PROFESSOR GUSTAVO GUANABARA

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', "quinze", 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número inteiro entre [0 e 20]: '))
    if 0 <= num <= 20:
        break
    print('Por favor, digite um número entre [0 e 20]!')
print(f'Você digitou o número {cont[num]}!')
'''