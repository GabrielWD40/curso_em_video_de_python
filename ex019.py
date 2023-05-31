#Um professor quer sortear um dos seus alunos para apagar o quadro.
#O programa deve ler o nome dos quatro alunos, depois deverá fazer um sorteio
# E mostrar o nome do aluno sorteado para apagar o quadro.
import random
print('=' * 40)
print('Sorteio de quem vai apagar o quadro. \nDigite o nome dos quatro participantes')
aluno_1 = input('Digite o primeiro nome: ')
aluno_2 = input('Digite o segundo nome: ')
aluno_3 = input('Digite o terceiro nome: ')
aluno_4 = input('Digite o quarto nome : ')
sorteado = [aluno_1.upper(), aluno_2.upper(), aluno_3.upper(), aluno_4.upper()]
# para abrir uma lista use o colchetes ['bolacha1, 'macarrão', 'leite']
print('\nO participante sorteado para apagar o quadro é {}'.format(random.choice(sorteado)))

"""
A função CHOICE retorna UM ELEMENTO selecionado ALEATORIAMENTE de uma SEQUÊNCIA ESPECÍFICA.
    para que você use-a, escreva da seguinte maneira: random.choice(sequencia)
        *IMPORTANTE: vc deve montar uma sequência antes de pedir para o algoritmo escolher aleatoriamente.
        
        Ele poderá escolher uma letra aleatoriamente de uma variável.
"""