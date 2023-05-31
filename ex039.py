"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
Conforme a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora
exata de se alistar ou se já passou do tempo do alistamento.
O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

ano_de_nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano_de_nascimento  # estou pegando o ano atual que a máquina fornece.
# O .YEAR significa que o progrma vai pegar o ano fornecido pelo dispositivo.
genero = str(input('Qual seu gênero? \nDigite M para masculino. \nDigite F para feminino.\n')).lower()
if genero == 'm':
    if idade == 18:
        print('Atualmente, você tem 18 anos e DEVE SE ALISTAR o MAIS BREVE POSSÍVEL a uma junta militar mais próxima.')

    # AQUI É A REGRA PARA QUANDO O JOVEM TEM MENOS DE 18 ANOS.
    elif idade <= 18:
        print('Ainda não é o momento de você se alistar no exército brasileiro!')
        if idade == 17:
            regra_17_anos = date.today().year + 1
            print('Falta 1 ano ainda! No momento você só tem 17 anos.'
                  '\nSeu ano de comparecimento deve ser só em {}'
                  '\nO alistamento deve ser feito quando você tiver completado 18 anos.'.format(regra_17_anos))
        else:
            ano_atual = date.today().year
            tempo_para_o_alistamento = ano_atual + (18 - idade)
            # aqui nessa variável eu calculo o ano que a pessoa deverá se alistar. Pego o ano atual e somo com quantos anos ele vai fazer 18 anos.
            print('\nSeu alistamento deverá ser feito somente em {}.'
                  '\nFaltam {} anos para você se alistar. '
                  '\nVocê tem {} anos no momento.'
                  '\n \nO alistamento deve ser feito quando você tiver 18 anos completos.'.format(
                tempo_para_o_alistamento, 18 - idade, idade))

    # FIM DA REGRA PARA QUEM TEM MENOS DE 18 ANOS.

    else:
        ano_atual = date.today().year  # estou pegando o ano atual da máquina
        prazo_de_alistamento_excedido = idade - 18  # subtraí da idade atual 18, aí retorna o valor de anos acima de 18.
        print('Atualmente, você tem {} anos. '
              '\nO ano do seu alistamento foi em {}.'
              '\nO seu prazo de alistamento já passou fazem {} anos.'.format(idade, (
                    ano_atual - prazo_de_alistamento_excedido), prazo_de_alistamento_excedido))
else:
    print('Por você ser uma mulher, não é obrigatório você se alistar no exército.')
