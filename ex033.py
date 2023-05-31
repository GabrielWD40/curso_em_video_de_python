"""
Esse algoritmo deve ler três valores digitados por um usuário.
Depois, ele deve ser capaz reconhecer os números digitados e dizer qual deles é o maior e o menor.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input("Digite o último número: "))
maior_numero = max(n1, n2, n3)
menor_numero = min(n1, n2, n3)

#verificando que é o maior:
print('Você digitou: {},{},{}'.format(n1, n2, n3))
if n1 > n2 and (n1 > n3):
    print('O número {} é o maior entre os números digitados!'.format(n1))
if n2 > n1 and (n2 > n3):
    print('O número {} é o maior entre os números digitados!'.format(n2))
if n3 > n1 and n3 > n2:
    print('O número {} é o maior'.format(n3))

#verificando que é o menor:
if n1 < n2 and (n1 < n3):
    print('O número {} é o menor entre os números digitados!'.format(n1))
if n2 < n1 and (n2 < n3):
    print('O número {} é o menor entre os números digitados!'.format(n2))
if n3 < n1 and n3 < n2:
    print('O número {} é o menor entre os números digitados!'.format(n3))

