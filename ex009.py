#esse algoritmo deve calculcar a tabuada de um número digitado até o 10 automaticamente sem while.
print('=' * 60)
n = int(input('Digite um número qualquer: '))
print('O número digitado foi {}, a tabuada de 0 até o 10 é: '.format(n))
print('{} x {:2} = {}'.format(n, 0, n * 0))
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))
#quando eu coloco {:2, significa que o objeto terá dois digitos. Por exemplo 1, ficará ' 1'.
# Ele terá um espaço antes do objeto
print('=' * 60)