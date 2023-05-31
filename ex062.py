"""
Exercício Python 62: Melhore o DESAFIO 61
perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

# REVISAR ESSE EXERCÍCIO MAIS TARDE. TIVE UM POUCO DE DIFICULDADE, MAS CONSEGUI 😎.
'Melhoria do exercício 61'
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o valor da razão: '))

contador = 0  # vai servir de base para começar o meu while
pa = primeiro_termo  # É a partir dessa variável que eu vou começar a calcular a progressão aritmética
numero_de_termos_da_pa = 0  # Vai receber +1 sempre que a progresão ganhar um novo termo.

colocacao_do_termo = 10  # O valor começa com 10 porque eu quero saber os 10 primeiros termos obrigatoriamente.
termos_a_mais = 1  # A variável tem que ter um valor acima de 0 para que o while funcione infinitamente.

while termos_a_mais != 0:  # Enquanto o usuário digitar um valor de cima, as condições abaixo se repetirão:
    while contador <= colocacao_do_termo:  # Enquanto o contador for menor ou igual colocação do termo faça as regras de baixo até o número do contador ter o mesmo valor que a posição do item.
        # Faça do 1 até chegar no 22, por exemplo.
        print('{} → '.format(pa), end='') #printa o valor atual da progressão
        pa += razao  # Atualiza o valor da PA a cada while, posição atual + razão
        contador += 1 # O contador ganha um ponto a cada realização, para saber quando parar.
        numero_de_termos_da_pa += 1  # Contabiliza quantos termos aparecem na PA.
    print('pause')
    termos_a_mais = int(input('Deseja mostrar mais quantos termos? '))  # O usuário escolhe mais quantos termos ele quer que apareça.
    colocacao_do_termo += termos_a_mais  # Soma 10 + o número digitado, mostrando novos resultados da PA.Se for 0, o programa se encerra.
print('Progressão aritimética encerrada. O total de termos digitados foi de {}'.format(numero_de_termos_da_pa))

