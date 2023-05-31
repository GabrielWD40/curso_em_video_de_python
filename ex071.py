"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('='*45)
print('Bem vindo aos sistemas bancários GS!')
valor = int(input('Quando você deseja sacar?\nR$: '))
div_temporaria = cedulas_de_50 = cedulas_de_20 = cedulas_de_10 = cedulas_de_1 = 0
while True:
    cedulas_de_50 = valor // 50
    div_temporaria = valor - (cedulas_de_50 * 50)
    cedulas_de_20 = div_temporaria // 20
    div_temporaria = div_temporaria - (cedulas_de_20 * 20)
    cedulas_de_10 = div_temporaria // 10
    div_temporaria = div_temporaria - (cedulas_de_10 * 10)
    cedulas_de_1 = div_temporaria // 1
    div_temporaria = div_temporaria - (cedulas_de_1)
    if div_temporaria == 0:
        break
print('='*45)
print(cedulas_de_50)
print(cedulas_de_20)
print(cedulas_de_10)
print(cedulas_de_1)