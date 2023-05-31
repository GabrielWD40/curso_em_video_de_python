"""
Esse algoritmo deve ler o salário de uma pessoa e aplicar um reajuste com base em quanto ela ganha.
Se o funcionário ganha mais de 1200 reais, o reajuste é de 10%
Se o funcionário ganha menos de 1200 reais, o reajuste é de 15%
"""

print('Vamos fazer um reajuste salarial para você:')
salario = float(input('Digite o valor do seu salário: R$ '))
if salario <= 1200:
    reajuste_1 = salario * 0.15
    print('Seu salário foi reajustado em 15%.\nVocê ganhou um aumento de {:.2f}, totalizando R${:.2f} reais.'.format(reajuste_1, (salario + reajuste_1)))
else:
    reajuste_2 = salario * 0.1
    print('Seu salário foi reajustado em 10%.\nVocê ganhou um aumento de {:.2f}, totalizando R${:.2f} reais.'.format(reajuste_2, (salario + reajuste_2)))
