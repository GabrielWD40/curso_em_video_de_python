"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""

print('\033[36m#\033[m'*120)
print('{:=^40}'.format(' DO HARDWARE AO SOFTWARE '))
"""
APRENDIZADO COM O PROFESSOR GUANABARA:
O ^ serve para centralizar os intens.
A expressão ^40 vai contralizar a formatação em quarenta espaços.
como eu coloquei =^40, ele vai centralizar o que eu disse no format mais o sinal de igual =
"""
print('\nO Valor total das suas compras está sujeito a mudanças de acordo com a forma de pagamento realizada.')
valor_das_compras = float(input('Digite o valor total das suas compras em R$ '))
print('Agora, selecione um método de pagamento:')
print('\n[ 1 ] - Para pagamentos à vista em dinheiro/cheque: 10% de desconto')
print('[ 2 ] - Para pagamentos à vista no cartão: 5% de desconto')
print('[ 3 ] - Para pagamentos em até 2x no cartão: preço formal')
print('[ 4 ] - Para pagamentos em 3x ou mais no cartão: 20% de juros')
opcao_escolhida = int(input('\nDigite a opção desejada: '))
if opcao_escolhida == 1:
    valor_do_desconto = valor_das_compras * 0.1
    compra_com_desconto = valor_das_compras - valor_do_desconto
    print('Você escolheu a opção 1: - Pagamento a vista em dinehiro/cheque.')
    print('Com o desconto de 10%=({:.2f}), o valor total da sua compra passa de (R${:.2f}) para \033[1m(R${:.2f})\033[m.'.format(valor_do_desconto, valor_das_compras, compra_com_desconto))
elif opcao_escolhida == 2:
    valor_do_desconto = valor_das_compras * 0.05
    compra_com_desconto = valor_das_compras - valor_do_desconto
    print('Você escolheu a opção 2: - Para pagamentos à vista no cartão: 5% de desconto')
    print('Com o desconto de 5%=({:.2f}), o valor total da sua compra passa de (R${:.2f}) para \033[1m(R${:.2f}).'.format(valor_do_desconto, valor_das_compras, compra_com_desconto))
elif opcao_escolhida == 3:
    print('\033[1mSUA MODALIDADE NÃO INCLUI NENHUM DESCONTO.\033[m')
    print('Você escolheu a opção 3: - Para pagamentos em até 2x no cartão: preço formal')
    valor_do_parcelamento = valor_das_compras / 2
    print('O valor total da \033[1msua compra(R$:{:.2f}) será dividido em duas parcelas mensais de R${:.2f}!\033[m'.format(valor_das_compras, valor_do_parcelamento))
elif opcao_escolhida == 4:
    valor_dos_juros = valor_das_compras * 0.2
    valor_total_com_juros = valor_das_compras + valor_dos_juros
    valor_das_parcelas = valor_total_com_juros
    print('\033[1mA SUA MOLIDADE INCLUI JUROS DE 20%!')
    print('O valor total das suas compras ficam em R$:{:.2f}'.format(valor_total_com_juros))
    numero_de_parcelas = int(input('Em quantas vezes você deseja fazer? '))
    valor_das_parcelas = valor_total_com_juros / numero_de_parcelas
    print('Você escolheu fazer a compra em {} vezes. Cada parcela terá o valor de R$ {:.2f}'.format(numero_de_parcelas, valor_das_parcelas))

else:
    print('\033[7;31mPor favor, digite uma opção válida!')
