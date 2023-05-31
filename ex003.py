n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
soma = n1 + n2
""" 
coleta de dados: é necessário converter a variável em "número inteiro" 
porque se não, ele concatena e faz uma junção de caracteres e não a soma.
LEMBRE-SE SEMPRE DE CONVERTER STRING EM INT OU FLOAT
"""

# resultado
# print('a soma dos números digitados é:', soma)

print('a soma de {} mais {} é igual a {}'.format(n1, n2, soma))
print(n1, type(n1))
print(n2, type(n2))
