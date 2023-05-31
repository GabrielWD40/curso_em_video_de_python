"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
print('{:*^33}'.format(' DO WARDWARE AO SOFTWARE '))
Quant_de_produtos_acima_de_1000_reais = 0
Nome_do_produto_mais_barato = None
Preço_do_produto_mais_barato = 0
Valor_total_da_compra = 0
Cont = 0
while True:
    Cont += 1
    nome_do_produto = str(input('Digite o nome do produto: ')).strip()
    preço_do_produto = float(input('Informe o valor do produto: R$ '))
    Valor_total_da_compra += preço_do_produto
    if Cont == 1:
        Nome_do_produto_mais_barato = nome_do_produto
        Preço_do_produto_mais_barato = preço_do_produto
    if preço_do_produto > 1000:
        Quant_de_produtos_acima_de_1000_reais += 1
    if preço_do_produto < Preço_do_produto_mais_barato:
        Nome_do_produto_mais_barato = nome_do_produto
        Preço_do_produto_mais_barato = preço_do_produto
    escolha = ' '
    while escolha[0] not in 'SN':
        escolha = str(input('Você deseja informar mais algum produto? [S/N] ')).upper().strip()
    if escolha[0] == 'N':
        break
print('='*60)
print(f'O preço total das suas compras é de R${Valor_total_da_compra:.2f}!')
print(f'No seu carrinho de compras existem {Quant_de_produtos_acima_de_1000_reais} produtos acima de R$ 1000.')
print(f'O item mais barato do seu carrinho chama-se {Nome_do_produto_mais_barato}, seu valor monetário é de R$ {Preço_do_produto_mais_barato:.2f}!')

"""
O professor Guanabara deu uma boa dica que tu podes usar entre as linhas 19 e 26
Por exemplo, ao invés de usar duas condicionais, use if cont == 1 or preço_do_produto < Preço_do_produto_mais_barato
"""


