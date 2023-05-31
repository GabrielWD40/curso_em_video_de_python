'''
Exercício Python 73:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

times_brasileirão = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro', 'Flamengo',
                     'Fluminense', 'Fortaleza', 'Bragantino', 'Atlético - PR', 'Santos', 'Internacional',
                     'Corinthians', 'Cuiabá', 'Bahia', 'Goiás', 'Vasco da Gama', 'América-MG', 'Coritiba')

print('Com base nos dados de 29/05/23 da tabela do Brasileirão:')
print('Os cinco primeiros times na tabela do brasileirão são:')
cont = 0
for cinco_colocados in times_brasileirão:
    cont += 1
    print(f'{cont}º = {cinco_colocados}')
    if cont == 5:
        break
print()

# Pegando os quatro últimos
print('Os quatro últimos times na tabela do brasileirão são:')
# Método do professor Guanabara: print(times_brasileirão[-4:])
# Ele vai pegar do 4º último item e mostrar daí em diante.
# Tipo, ele vai pegar do -4 e vai mostrar tudo daí em diante.
print(f'Em 20º lugar = {times_brasileirão[-1]}')
print(f'Em 19º lugar = {times_brasileirão[-2]}')
print(f'Em 18º lugar = {times_brasileirão[-3]}')
print(f'Em 17º lugar = {times_brasileirão[-4]}')
print()

# Deixando em ordem alfabética
print('Os times em ordem alfabética são: ')
print(sorted(times_brasileirão))
print()

# Especificando um item:
print(f'Posição do time do atlético paranaense na primeira divisão: {times_brasileirão.index("Atlético - PR")+1}º lugar!')