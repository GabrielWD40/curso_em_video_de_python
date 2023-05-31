texto = input("Digite alguma coisa: ")

print("a variável que você digitou é do tipo: ", type(texto))
print("O que você digitou é um alfa-numérico: ", texto.isalnum()) #checa a variável se é alfa numérico 1a, 4a,2, f ...
print("O que você digitou é somente letras: ", texto.isalpha()) #checa a variável se é somente letras
print("O que vc digitou é printável:", texto.isprintable()) #checa a variável pode ser printável
print('o que você digitou está tudo em maiúsculo:', texto.isupper())#checa a variável é toda maiúscula
print('o que você digitou está tudo em minúsculo:', texto.islower())#checa a variável é toda minúscula
print('o que você digitou é somente um número:', texto.isnumeric())#checa a variável é toda numérica
print(f'o que você digitou é um espaço: {texto.isspace()}')#checa a variável é um espaço
print('o que você digitou é um número decimal:', texto.isdecimal())#checa a variável é  decimal
print(f"O que você digitou começa com maiúsculo e o resto é todo minúsculo: {texto.istitle()}")#  #checa a variável é título que começa com maiúscula e termina com tudo minúsculo.
print(f'Está capitalizado? {texto.istitle()}')
#as variáveis são objetos tem uma característica que realiza funcionalidades. Toda string tem esse métodos, os parenteses.
#eu alternei entre o formato mais novo e o mais velho.