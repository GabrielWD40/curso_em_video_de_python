"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal
"""
numero = int(input('Digite um número inteiro qualquer: '))
print('Digite 1 para converter {} para binário.'.format(numero))
print('Digite 2 para converter {} em octal.'.format(numero))
print('Digite 3 para converter {} em hexadecimal.'.format(numero))
escolha_de_opcao = int(input('Digite o número da sua opção: '))
if escolha_de_opcao == 1:
    conversao = bin(numero)#bin converte o número pra binário
    print('{} representado em binário fica {}'.format(numero, conversao[2:]))
    #estou utilizando o fatiamento pra tirar o prefixo e só aparecer a conversão.
elif escolha_de_opcao == 2:
    conversao = oct(numero) #oct converte o número pra octal
    print('{} representado em octal fica {}'.format(numero, conversao[2:]))
    #estou utilizando o fatiamento pra tirar o prefixo e só aparecer a conversão.
elif escolha_de_opcao == 3:
    conversao = hex(numero) # hex converte o número pra hexadecimal
    print('{} representado em hexadecimal fica {}'.format(numero, conversao[2:]))
    #estou utilizando o fatiamento pra tirar o prefixo e só aparecer a conversão.
else:
    print('A opção digitada é inválida!')

#em python ele traz um prefixo nas casas 0 e 1 que indicam tipo de conversão, tipo 0b que é pra binário.
#Pra fazer esse prefixo sumir, o professor Guanabara utilizou o fatiamento de strings.
#Então tudo que vier depois da casa 2, será exposto e como eu não defini um final, ele vai pegar tudo.
