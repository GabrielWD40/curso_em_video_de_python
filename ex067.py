"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""
numero = 0
while True:
    print('\033[34m=\033[m'*60)
    numero = int(input('Digite um número para ver a sua tabuada: '))
    if numero < 0:
        break
    for tabuada in range(1, 11):
        resultado = numero * tabuada
        print(f'{numero} x {tabuada} = {resultado}')
print('FIM DO PROGRAMA! volte sempre!')
