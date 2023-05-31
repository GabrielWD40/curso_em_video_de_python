"Esse exercício deve ler um nome de cidade retornar o valor verdadeiro se ela começar com Santo..."

print('Verificando se o nome da cidade digitada começa com Santo.')
cidade_de_nascimento = str(input('Em qual cidade você nasceu? ').strip())
formatacao_da_cidade = cidade_de_nascimento.title()
print('O nome da cidade que você é: {}\nEla começa com Santo? {}'.format(formatacao_da_cidade, formatacao_da_cidade.startswith('Santo') ))