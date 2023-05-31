"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.
"""

from datetime import date

# Resolução média das idades:
ano_atual = date.today().year  # Pega o ano atual.
soma_das_idades = 0  # Variável que será usada para somar as idades.

# Resolução do problema para os homens
nome_do_homem_mais_velho = None  # Variável que vai guardar o nome do homem mais velho, caso haja um.
idade_do_homem_mais_velho = 0  # Variável que vai guardar a idade do homem mais velho, caso haja um.

# Resolução para o problema das mulhres
numero_de_mulheres_menores_de_idade = 0  # Variável que vai guardar o número das mulheres abaixo de 18 anos.
numero_de_mulheres = 0  # Número de mulheres cadastradas. Mais tarde será usado para informar se há mulheres.

for iteracao in range(1, 5):
    nome = str(input('Digite o \033[1;33mnome da {}ª pessoa\033[m: '.format(iteracao))).strip().title()  # Pegando o nome da pessoa.
    ano_de_nascimento = int(input('Digite o \033[1;33mano de nascimento da {}ª pessoa\033[m: '.format(iteracao)))  # Pegando o ano de nascimento da pessoa.
    idade = ano_atual - ano_de_nascimento  # Calculando a idade da pessoa com base no ano atual da máquina.
    soma_das_idades += idade  # Variável que soma todas as idades digitadas para depois fazer a média.
    genero = str(input('Digite o\033[1;33m gênero da {}ª pessoa\033[m\nUse \033[1;33m"M" para masculino\033[m ou \033[1;33m"F" para feminino\033[m: '.format(iteracao))).upper()  # Pegando o gênero da pessoa para poder fazer as regras condicionais.

    if iteracao == 1 and genero == 'M':  # Quando tiver rolando primeiro looping e o gênero da pessoa for masculino:
        nome_do_homem_mais_velho = nome  # A variável "nome_do_homem_mais_velho" recebe o nome digitado no primeiro looping.
        idade_do_homem_mais_velho = idade  # A variável "idade_do_homem_mais_velho" recebe a idade digitada no primeiro looping.

    if genero == 'F':  # Se o gênero for feminino, a variável número recebe +1. Que mais tarde ajudará a identificar quantas mulheres existem no cadastro.
        numero_de_mulheres += 1

    if idade > idade_do_homem_mais_velho and genero == 'M':  # Se o valor da idade digitada for maior do que está na "idade_do_homem_mais_velho" e o gênero for masculino:
        nome_do_homem_mais_velho = nome  # A variável "nome_do_homem_mais_velho" recebe o nome digitado no looping atual.
        idade_do_homem_mais_velho = idade  # A variável "idade_do_homem_mais_velho" recebe a idade digitada no loopiing atual.
    # Essa regra serve para quando você cadastra um homem mais velho que os outros cadastrados anteriormente. Ou então, quando decide cadastrar um homem em um dos loopings.

    if genero == 'F' and idade < 18:  # Regra para quando uma mulher menor de 18 anos for cadastrada:
        numero_de_mulheres_menores_de_idade += 1  # A variável "numero_de_mulheres_menores_de_idade" recebe 1 ponto para cada mulher menor de idade.
    print()
    print('\033[33m=\033[m'*60)  # Deixando o código mais bonito.
    print()

"  ******   MOSTRANDO RESULTADOS PARA O USUÁRIO   ******  "

media_idade_do_grupo = soma_das_idades / 4  # A variável "media_idade_do_grupo" calcula a média de idade do grupo com um todo.
                                            # Ela recebe o valor das somas das idades e divide pelo número de integrantes do grupo.

if nome_do_homem_mais_velho is None:  # Caso não haja nenhum homem cadastrado, a mensagem abaixo é retornada.
    print('\033[1;31mVocê não incluiu nenhum homem no cadastro.\033[m')
else:   # Caso contrário, há um homem cadastrado. Então, o bloco de baixo é executado.
    print('O homem mais velho se chama: {}, ele tem {} anos de idade!'.format(nome_do_homem_mais_velho, idade_do_homem_mais_velho))

print('A média de idade do grupo é de {} anos! '.format(media_idade_do_grupo))  # Nessa etapa, mostramos ao usuário a média das idades do grupo cadastrado.

# Regra para as mulheres:
if numero_de_mulheres == 0:  # Se o número de mulheres for igual a 0:
    print('\033[1;31mVocê não incluiu nenhuma mulher no cadastro.\033[m')
elif numero_de_mulheres_menores_de_idade == 0:  # Se a variável "numero_de_mulheres_menores_de_idade" for igual a 0:
    print('Não há nenhuma mulher menor de 18.')
else:  # Se as condições acima forem falsa, há mulheres menos de 18 anos nesse cadastro.
    print('Número de mulheres abaixo de 18 anos: {}'.format(numero_de_mulheres_menores_de_idade))
