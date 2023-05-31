#esse algoritmo deve mostrar o dobro tripo e a raiz quadrada de um número.
n = int(input('Digite um número inteiro: '))

print('O dobro de {} é = {}!'.format(n, n*2), end='\nO triplo de {} é = {}'.format(n, n*3))
print(" ")
print('A √{} é igual a {:.2f}!'.format(n, n**(1/2)))