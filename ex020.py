#esse algoritmo deve definir a ordem de apresentações dos trabalhos dos alunos aleatoriamente.
from random import shuffle
print('=' * 40)
print('Sorteio aleatório da ordem de apresentação dos trabalhos. \nDigite o nome dos quatro participantes')
aluno_1 = input('Digite o primeiro nome: ')
aluno_2 = input('Digite o segundo nome: ')
aluno_3 = input('Digite o terceiro nome: ')
aluno_4 = input('Digite o quarto nome: ')
lista_de_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_de_alunos) #shuffle=embaralhar
#random.shuffle serve para embaralhar uma ordem.
print('A ordem de apresentação será: \n{}'.format(lista_de_alunos))
