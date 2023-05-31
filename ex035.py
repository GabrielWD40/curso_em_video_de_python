"""
Esse algoritmo deve conseguir ler 3 valores e verificar se eles formam um triângulo.
Além disso, se os números formaram um triângulo, o seu ‘software’ deverá mostrar qual o tipo dele.
Se não formar, deverá trazer a mensagem de que não forma triângulo.

Regras dos triângulos, a soma de dois lados deve ser maior que um lado.
a+b>c
b+c>a
c+a>b
"""
print('-*-'*30)
print('Vamos verificar se as retas A, B e C formam um triângulo.')
lado_a = float(input('Digite o valor do lado A: '))
lado_b = float(input('Digite o valor do lado B: '))
lado_c = float(input('Digite o valor do lado C: '))
if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Os as retas A={}, B={} e C={} formam um triângulo!'.format(lado_a, lado_b, lado_c))
else:
    print('Os lados A={}, B={} e C={} NÃO FORMAM um triângulo!'.format(lado_a, lado_b, lado_c))
print('-*-'*30)
