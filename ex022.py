"""
O exercício deve:
1-converter todo o nome para maiúsculo (ok)
2-converter todo o nome para minúsculo (ok)
3-Indicarcar quantas letras o nome tem sem contar os espaços. (ok)
4-Quantas letras tem o primeiro nome. ()
"""

nome = str(input('Digite um nome completo qualquer: '))
print('o nome digitado foi: {} '.format(nome))

nome_maiuscilo = nome.upper().strip() #converte tudo pra maiúsculo eliminando os espaços em branco
nome_minúsculo = nome.lower().strip() #converte tudo pra minúsculo eliminando os espaços em branco
nome_sem_espacos = nome.strip() #Deixa o nome sem espaços.
numero_de_letras = len(nome_sem_espacos.replace(" ","")) # primeiro, ele tira todos os espaços, depois conta tudo junto.
#Uma outra forma de resolver o problema de contafem de letras seria len(nome) - nome.count(" ")

print('O nome todo em maiúsculo fica: {}.\nO nome todo em minúsculo fica: {}.'.format(nome_maiuscilo, nome_minúsculo))
print('Além disso, o nome {} tem {} letras.'.format(nome.upper().strip(), numero_de_letras))

nome_dividido = nome.split() #aqui o python divide o nome todo em tabelas.
print('O primeiro nome digitado foi {}, ele tem {} letras.'.format(nome_dividido[0].upper(), len(nome_dividido[0])))

#Método de resolução da 3 coisa: usar a fução strip pra tirar todos os espaços inúteis
#depois, transformar em tabelas e somar td. Na teoria, vamos resolver o número quatro com isso.

