""""
Esse algoritmo deve procurar se a pessoa tem o sobrenome SILVA no seu nome completo.
"""

print('Vamos verificar se você tem silva no nome.')
nome_completo = str((input('Informe o seu nome completo: ').strip()))
nome_formatado = (nome_completo.title())
teste =('Silva' in nome_formatado)
#aqui tivemos que usar o IN. Use ele quando vc precisa encontrar um valor específico para uma string.

print('O resultado do nome {} possuir SILVA é: {}'.format(nome_formatado, teste))
