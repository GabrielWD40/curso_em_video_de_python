# faça um programa que leia os comprimentos dos catetos oposto djacente do TRIÂNGULO RETÂNGULO
# Calcule e mostre o comprimento da hipotenusa
import math

print('Calculando os catetos e o comprimento da hipotenusa: ')
base = float(input('Digite um valor para ao cateto adjacente: '))
altura = float(input('Digite um valor para o cateto oposto: '))
    #hipotenusa = math.sqrt((lado_1 ** 2 + lado_2 ** 2))
hipotenusa = math.hypot(base, altura)
    #A função hypot é usada para encontrar a hipotenusa de um triângulo retângulo
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))

""" 
Para encontrar o valor de um dos catetos vc precisa ter o valor da hipotenusa:
    cateto 1= 3
    Hipotenusa= 5
    cateto 2= ?
    
    1º passo, soma os valores que vc tem:
        5+3=8
        
    2º passo, diminua os valores que você possui, hipotenusa - cateto:
        5-3=2
        
    3º passo, faça o resultado do 1º passo vezes o resultado do 2º passo e depois tire a raiz quadrada.
        √8*2
        
    Na prática, ficaria assim: 
        cateto_misterioso= √((cateto_1 + hipotenusa)*(hipotenusa-cateto_1))
        
"""