"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
soma_dos_numeros_pares = 0
total_de_numeros_pares = 0
for estrutura_de_iteracao in range(1, 7):
    # A variável (estrutura_de_iteracao) tem o valor 6, isso quer dizer que ela vai repetir o que está dentro dela 6 vezes.
    # Se você pedir pra imprimir essa variável, ele trará o número 6
    numero = int(input('Digite o {}º número: '.format(estrutura_de_iteracao)))
    if numero % 2 == 0:  # verifica se um dos números digitados é par.
        soma_dos_numeros_pares = numero + soma_dos_numeros_pares  # Se for par, ele soma esses valores dentro da variável.
        total_de_numeros_pares = total_de_numeros_pares + 1
print('O total de números pares digitados é = {} e a soma entre eles é de {}.'.format(total_de_numeros_pares, soma_dos_numeros_pares))