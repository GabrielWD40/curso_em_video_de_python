"""
Exercício Python 47: Crie um programa que mostre na tela
todos os números pares que estão no intervalo entre 1 e 50.
"""

for numeros_duplos in range(0, 51, 2):
    print(numeros_duplos, end=' ')
    #utiliza menos processamento.
print()

for numeros_duplos in range(0, 51):
    if numeros_duplos % 2 == 0:
        # Utiliza mais processamento
        print(numeros_duplos)

