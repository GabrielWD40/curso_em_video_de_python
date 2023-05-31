"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
print("VERIFICADOR DE PALÍNDROMO")
for verificador_de_palindromo in range(1):
    frase = str(input('Digite alguma frase: \n').strip())  #Captura uma frase do usuário e remove os espaços inúteis que tem antes e depois da frase.
    frase_formatada = frase.lower().replace(' ', '')  #Formata a frase toda para minúsculo e tira os espaços. Fiz isso para facilita!
    frase_formatada_invertida = frase_formatada[::-1] #Aqui a variável recebe a frase toda formatada só que ao inverso!
    if frase_formatada == frase_formatada_invertida:
        print('A frase "\033[1;33m{}\033[m" \033[1;32mÉ UM PALÍNDROMO!!\033[m'
              '\n{} = {}!'
              '\n{} = {}!'.format(frase.upper(), frase_formatada, frase_formatada_invertida, frase.lower(), frase.lower()[::-1]))
    else:
        print('A frase "\033[1;33m{}\033[m" \033[1;31mNÃO É UM PALÍNDROMO!\033[m'.format(frase.upper()))
