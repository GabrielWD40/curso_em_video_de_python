"""
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999 equivalente condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
total_de_numeros_digitados = soma = numero = 0
while True:
    numero = int(input('Digite um valor qualquer(use 999 para parar): '))
    if numero == 999:
        break
    soma += numero
    total_de_numeros_digitados += 1
print(f'A soma dos {total_de_numeros_digitados} números digitados  é = {soma}!')