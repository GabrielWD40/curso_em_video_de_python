"""
Exercício Python 63: Escreva um programa que leia um número N inteiro
qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
"""

# print('{:^40}'.format('Sequência de Fibonacci'))
print('=-=' * 20)
print('Sequência de Fibonacci!')
numero_de_termos = int(input(
    'O valor de qual termo você deseja saber? '))  # Captura até que termo o usuário quer que a sequência seja exibida.
t1 = int(0)  # O primeiro termo é sempre 0. Por isso ele começa valendo 0.
t2 = int(1)  # O segundo termo é sempre 1. Por isso, ele começa valendo 1.
t3 = 0  # O terceiro termo é sempre a soma do primeiro mais o segundo termo. E assim, sucessivamente no resto da sequência.

if numero_de_termos == 1:
    print('{}'.format(t1))

elif numero_de_termos == 2:
    print('{} → {}'.format(t1, t2))

elif numero_de_termos == 3:
    t3 = t1 + t2
    print('{} → {} → {}'.format(t1, t2, t3))
else:
    contador = 2
    # O contador começa sempre em 2, pois já começamos a exibir tudo a partir do segundo termo. Ele é o parâmetro para começar o 'while'
    print('{} → {} → '.format(t1, t2), end='')  # Aqui eu estou imprimindo os dois primeiro termos e imendando com o que vem mais para baixo.
    while contador <= numero_de_termos:
        # Aqui ele o número de termos recebe menos dois porque eu já estou exibindo os dois primeiros.
        # Se eu deixar o número de termos sem uma subtração de -2, ele exibe termos a mais dos que os que foram pedidos.
        # Se a pessoa digita 10, ele faz mais 10 termos além dos que já existem.
        t3 = t1 + t2
        contador += 1
        print('\033[34m{} → '.format(t3), end='')
        t1 = t2
        t2 = t3
    print('FIM!')
