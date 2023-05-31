"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print('PROGRESSÃO ARITIMÉTICA:')
numero = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razão dessa P.A? '))
sequencia = numero
while sequencia <= (numero + (10 * razao)):
    print('{} → '.format(sequencia), end='')
    sequencia += razao
print('FIM!')

print()
print()

"solução do Guanabara:"
primeiro = int(input('Digite o primeiro termo: '))
razaoao = int(input('Digite o segundo termo: '))
termo = primeiro  # parecido com o meu, é o que vai gerar aquela sequência toda.
contador = 1  # será usado na estrutura de repetição.

while contador <= 10:
    print('{} → '.format(termo), end='')
    termo += razaoao
    contador += 1
print('FIM!')