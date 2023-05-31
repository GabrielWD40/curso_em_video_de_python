"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
print('Verificando o maior e menor peso digitados:')
lista_de_pesos_digitados = []
for iteracao in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (KG): '.format(iteracao)))
    lista_de_pesos_digitados.append(peso)
maior_peso = max(lista_de_pesos_digitados)
menor_peso = min(lista_de_pesos_digitados)
print('O MAIOR peso digitado foi: {}!'.format(maior_peso))
print('O MENOR peso foi digitado: {}!'.format(menor_peso))
print('\n')
print('\n')




" *********** MÉTODO DO GUANABARA *********** "

maior = 0
menor = 0
for p in range(1, 7):
    peso = float(input('Digite o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso digitado foi: {}'.format(maior))
print('O menor peso digitado foi: {}'.format(menor))

" ********* FIM MÉTODO DO GUANABARA ********* "