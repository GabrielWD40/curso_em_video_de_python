"""
Esse algoritmo deve ser capaz de contar quantas letras A´s aparecem numa frase aleatória digitada
Qual a posição que ela aparece pela primeira vez
Qual a posição que ela aparece por último
"""

print('Vamos contar quantas letras A aparecem na sua frase! ')
frase = str(input('Digite uma frase qualquer: ').lower().strip())
numero_de_letras_a = "Sua frase tem " + str(frase.count('a')) + " letras A."
primeira_letra_a = frase.find("a")+1
#coloquei o +1 pra ficar mais fácil de um usuário entender. Porque eu sei o que é posição 0, ele não. Daí fica confuso.
ultima_letra_a = frase.rfind('a')+1
#IMPORTANTE
#lembre-se de usar os operadores LFIND e RFIND
#No primeiro ele começa procurar da esquerda para a direita e vice-versa.
#Nesse exemplo o professor mostroua solução com o rfind.O mais um servirá para faciliatar o entendimento do usuário por causa da casa 0

print(numero_de_letras_a)
print('A primeira letra A apareceu na posição {}.'.format(primeira_letra_a))
print('A última letra A apareceu na posição {}.'.format(ultima_letra_a))

