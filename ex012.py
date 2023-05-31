#esse algoritmo deve ler o preço de um produto e depois aplicar um cupom de 5% de desconto
#mostrando o novo preço com o desconto.

print('Digite um valor para um produto, depois, aplicaremos 5% de desconto.')
valor = float(input('Digite um valor em R$: '))
desconto = 0.05

print('O valor final do produto X passou de R${} para R${:.2f} após receber 5% de desconto.'.format(valor, valor-(desconto * valor)))