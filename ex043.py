"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

from time import sleep

print('-*-' * 35)
print('CALCULADORA DE IMC')
altura = float(input('Digite a sua alteura em metros: '))
peso = float(input('Digite o seu peso em KG: '))
# , end='' usa isso para alinhar com a linha de baixo.
print('\n*** Calculando o seu IMC ***')
sleep(3)  # o programa dorme por 5 segundos.
imc = float(peso / (altura ** 2))

if imc < 18.5:
    print('Atualmente, \033[4;31mseu IMC é {:.2f}\033[m.'.format(imc))
    print('\nVocê está \033[4;31mABAIXO DO PESO IDEAL!\033[m'
          '\nVocê deve se alimentar melhor.')
elif 18.5 < imc <= 25:
    print('Atualmente, \033[4;32mseu IMC é {:.2f}\033[m.'.format(imc))
    print('Você está com o \033[4;32mPESO IDEAL\033[m.'
          '\nParabéns, continue assim!')
elif 25 < imc <= 30:
    print('Atualmente, \033[4;33mseu IMC é {:.2f}\033[m.'.format(imc))
    print('Você está com \033[4;33mSOBREPESO\033[m.'
          '\nCuidado! Você está acima do peso.')
elif 30 < imc <= 40:
    print('Atualmente, \033[4;31mseu IMC é {:.2f}\033[m.'.format(imc))
    print('\033[4;31mVocê está com OBESIDADE!\033[m'
          '\nMude a sua alimentação e se cuide mais.')
else:
    print('Atualmente, \033[4;31mseu IMC é {:.2f}\033[m.'.format(imc))
    print('\033[4;31mVocê está com OBESIDADE MÓRBIDA!\033[m'
          '\nVOCÊ PRECISA SE CUIDAR MAIS.')
