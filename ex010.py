#esse algoritmo deve ler quanto dinheiro uma pessoa tem na carteira e quanto dólares ela consegue comprar com esse valor
# cotação = 3,27
print('=' * 60)
print("programa que calcula a cotatização do real para o dólar (3,27).")
d = float(input('Quantos reais você deseja converter?'))
print('Fazendo a conversão de R$ {}, você conseguirá comprar USD$ {:.2f} dólares americanos;'.format(d, d/3.27))