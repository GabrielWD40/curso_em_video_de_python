#esse programa deve mostrar o sucessor e o antecessor do número digitado.
n1 = int(input('digite um número inteiro: '))
sucessor = n1 + 1
antecessor = n1 -1

print('O sucessor de {}, é {}'.format(n1, sucessor), end=' e o seu antecessor é {}!'.format(antecessor))
