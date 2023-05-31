"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('** TABUADA **')
numero = int(input('Digite um número: '))
for tabuada in range(0, 11):
    multiplicacao = numero * tabuada
    print('{} x {} = {}'.format(numero, tabuada, multiplicacao))
"""

numero = int(input('Digite um número inteiro qualquer para ver a sua tabuada: '))
for tabuada in range(1, 11):
    print('{} x {} = {}'.format(numero, tabuada, numero*tabuada))

"""
Tive dificuldade de entender como eu faria a multiplicação.
Vou tentar me auto-explicar.

A variavel tabuada vai do 1 ao 10, ela tem todos esses dados.
Pra fazer a tabuada eu preciso de um numero qualquer.
Depois disso, eu armo a barraca dentro da estrutura de iteração.
Isso é, pego o número que eu pedi e faço a multiplicação pela variável do for;

E como ele vai ficar repetindo até chegar no número que eu defini, tudo fica automático.

lembre-se que a variável entre for e in é muiuto importante.
"""