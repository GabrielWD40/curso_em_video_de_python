#faça um algoritmo que mostre o salário de um trabalhador, depois mostre esse mesmo salário com um reajuste de
#15% de aumento.

print("=" * 50)
print('calculadora de reajuste salarial de 15%')
sal = float(input('Digite o seu salário atual em R$: '))
reajuste = 0.15
#é possível fazer assim: salário * 15 /100

print("O seu novo salário é de R$ {:.2f}! \n \nSeu salário foi reajustado em {:.2f} Reais".format((sal*reajuste) + sal, (sal*reajuste)))
