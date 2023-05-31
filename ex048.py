"""
Exercício Python 48: Faça um programa que calcule a soma entre
todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Soma de todos os múltiplos de 3 de 1 a 500.')
"""

numeros_impares = 0  # Criei uma variável com o valor 0. É ela quem vai receber os valores ímpares.
multiplos_de_3 = 0  # Criei uma variável com o valor 0, pois ela vai receber os valores ímpares e que são multiplos de 3.
contagem_dos_multiplos_de_três = [] # essa é uma lista que armazena todos os múltiplos e depois fará a contagem deles.

for numeros in range(0, 501):
    if numeros % 2 != 0: # Aqui eu estou verificando se o número é ímpar. Se sim, ele executa o bloco de baixo. Se não, ignora.
        numeros_impares = numeros # Se a condição for verdadeira, a variável recebe esses números.
        if numeros_impares % 3 == 0: # Aqui eu abro mais uma condição, se os números ímpares armazenados são múltiplos de 3;

            contagem_dos_multiplos_de_três.append(numeros_impares)# aqui eu estou dizendo que a minha lista receberá todos os múltilpos de três
            #a sintaxe é o nome-da-lista.append[que irá adicionar o último valor na lista.].(intervalo de onde eu estou pegando a regra.)

            multiplos_de_3 += numeros_impares # Aqui a variável multiplos de três está recebendo os valores multiplos de 3 e somando-os.
print('A soma dos {} multiplos de 3 no intervalo de 1 a 500 é = {}!'.format(len(contagem_dos_multiplos_de_três), multiplos_de_3))

"""
MÉTODO DO PROFESSOR GUANABARA: 
soma = 0 #faz a soma dos multiplos
cont = 0 #faz a contagem de números.
for c in range(1, 501,2)
    if c % 3 == 0:
        soma =+ c #aqui ele vai somando todos os valores, vai acumulando.
        cont =+ 1 #aqui cada vez que um número satisfaz a regra, ele soma mais um.
print('A soma de todos os {} solicitados é igual a {}.format('cont, soma'))
            
"""
