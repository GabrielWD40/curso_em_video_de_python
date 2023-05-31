"""
Esse algoritmo deve calcular se um ano é ou não é bissexto.
Pode ser qualquer ano
"""
from datetime import date

print('*' *40)
print('Verificador de ano bissexto')
ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year #Se o usuário digitar que o ano é 0, o python pega o ano atual da máquina e usa como referência.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #essa é a fórmula correta, porque um ano bissexto tem que ser divisivel por 4 e 400.
# != representa "diferente de"
    print('{} É UM ano BISSEXTO.'.format(ano))
else:
    print('{} NÃO É um ano BISSEXTO.'.format(ano))

"""
Nós vamos implemetar um código que o professor Guanabara ensinou:
 vamos importar uma classe DATETIME que servirá para pegar as datas direto da máquina.

    NO início do nosso código, vamos implemtar o seguinte código
    from datetime import date
    
    if ano ==0:
    ano = date.today().year
"""