#esse programa deverá ler um ângulo qualquer
#Depois ele deverá mostrar o seno e cosseno e tangente do ângulo

from math import cos, tan, sin, radians, ceil
angulo = radians(float(input('Digite o valor de um ângulo qualquer para calcularmos o seno, cosseno, tangente. \nValor do ângulo é = ')))
#É preciso converter
tangente = tan(angulo)
cosseno = cos(angulo)
seno = sin(angulo)
print('\nSENO: {:.2f} \nCOSSENO: {:.2f} \nTANGENTE: {:.2f}'.format(seno, cosseno, tangente))
"""
OBS: usei o arredondamento pra cima (ceil) para ficar como nos padrões da matemática:

tangente = ceil(tan(angulo))
cosseno = ceil(cos(angulo))
seno = ceil(sin(angulo))

Só que ele vai lançar uns números bem doidos, com várias casas decimais.
"""
