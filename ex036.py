"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from time import sleep

print('\033[1;36m-*-\033[m'*30)
print('ANÁLISE DE EMPRÉSTIMO BANCÁRIO PARA AQUISIÇÃO DE UM IMÓVEL.')
nome = str(input('Qual é o seu nome? ')).title()
salario_mensal = float(input('Informe o valor do seu salário: \n(R$): '))
valor_do_imovel = float(input('Qual o valor em R$ do imóvel? '))
numero_de_parcelas = int(input('Em quantas anos você pretende quitar o financiamento? '))*12
valor_da_prestacao = float(valor_do_imovel/numero_de_parcelas)
verificador_de_emprestimo = float(salario_mensal * 0.3)
print('\n \033[1;36m*** CALCULANDO RESULTADOS ***\033[m \n')

sleep(4)

if valor_da_prestacao > salario_mensal * 0.3: #aqui é se o valor da parcela excer os 30% do salário do cliente.
    print('\033[4;31m EMPRÉSTIMO NEGADO! \033[m')
    print('O valor das parcelas são de: \033[4mR$ ({:.2f})\033[m. '
          '\nO valor das parcelas \033[4mexcedem 30% do seu salário:({:.2f}).\033[4m\n'.format(valor_da_prestacao, verificador_de_emprestimo))
    # Para formatar com casas decimais, use ":.(numero de casas que queres)f → :.2f"

elif valor_da_prestacao == salario_mensal * 0.3: #aqui é se o valor da parcela for igual a 30% do salário do cliente.
    #pra calcular a porcentagem da pra fazer assim valor * número de percentural / 100
    print('\033[4;31mEMPRÉSTIMO NEGADO!\033[m')
    print('O valor das parcelas ficam em R$({:.2f}).\nPorém, o valor da parcela é igual a 30% do seu salário ({'
          ':.2f}).\n\033[4;31mDevido a isso, não será possível realizar o empréstimo.\033[m\n'.format(
        valor_da_prestacao, verificador_de_emprestimo))
else:
    print('\033[4;32mEMPRÉSTIMO APROVADO!!\033[m')
    print('Parabéns, {}! O empréstimo foi pré-aprovado em seu nome!'.format(nome))
    print('O valor das parcelas ficam em R$({:.2f}).\n'.format(valor_da_prestacao))
print('\033[1;36m-*-\033[m'*30)
