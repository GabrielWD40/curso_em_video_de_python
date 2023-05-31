"""
Esse programa deve fazer escolher um número de 0 a 5.
Depois, ele deve fazer o usuário tentar advinhar o que ele pensou.
Se ele acertar deve retornar uma mensagem de acerto
Se não, deve retornar uma mensagem de que ele errou.
"""
from random import randint
from time import sleep #a função "SLEEP" meio que faz o computador dormir, ele enrola um pouco.

numero_escolhido = randint(0, 5) #O PC escolher um número entre 0 e 5.
numero_chutado = int(input(('Tente adivinhar qual o número que o computador está pensando.\nChute um número de 0 a 5: ')))
print('PROCESSANDO O RESULTADO...')
sleep(2) #aqui eu estou falando pro computador esperar 2 segundos antes de mostrar o resultado.
if numero_chutado == numero_escolhido:
    print('VOCÊ ACERTOU!PARABÉNS')
else:
    print("VOCÊ ERROU!")
    print('O Número era {}'.format(numero_escolhido))

"""
FORMA QUE EU FIZ: 

import random
#from random import randint

lista = [0,1,2,3,4,5]
numero_escolhido = random.choice(lista)

numero_chutado = int(input(('Tente adivinhar qual o número que o computador está pensando.\nChute um número de 0 a 5: ')))
if numero_chutado == numero_escolhido:
    print('VOCÊ ACERTOU!PARABÉNS')
else:
    print("VOCÊ ERROU!")
    print('O Número era {}'.format(numero_escolhido))    
"""