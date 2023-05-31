"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""

print('Vamos verificar se as retas A,B e C formam um triângulo e de qual tipo.')
a = float(input('Digite um valor par o lado A: '))
b = float(input('Digite um valor para o lado B: '))
c = float(input('Digite um valor para o lado C: '))

if a < b + c and b < a + c and c < a + b:
    print('As retas A= {}, B= {} e C= {} \033[32mFORMAM UM TRIÂNGULO!\033[m'.format(a, b, c))
    if a == b and b == c:  # o python permite fazer a == b == c
        print('O trinângulo formado é o EQUILÁTERO')
        #se vc quiser jogar a linha de baixo no mesma linha de cima use (, end ="")
        print('Triângulo Equilátero: Possui todos os lados iguais.')
        if a == b or c == a or b == c:
            print('\nO trinângulo formado também é ISÓSCELES!')
            print('Triângulo Isósceles: Possui dois lados iguais.')
    elif a == b or c == a or b == c:
        print('O trinângulo formado é o ISÓSCELES!')
        print('Triângulo Isósceles: Possui apenas dois lados iguais.')
    else:  #se vc fosse fazer o escaleno, faria a != b != c != a
        print('O triângulo formado é o ESCALENO.\nÉ aquele que nenhum lado é igual!')
else:
    print('As retas A= {}, B={} e C= {} \033[31mNÃO FORMAM UM TRIÂNGULO!'.format(a, b, c))
