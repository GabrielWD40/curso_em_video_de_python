#esse algoritmo deve ler a altura e largura de uma parede em metros, calcule a área e quantidade de tinta
#ncessário para pintar essa parede sabendo que cada litro de tinta pinta 2m²

print('=' * 70, '\nVamos calcular quantos litros de tinta são necessários para pintar uma parede! \n Sabendo que cada litro de tinta pintam 2m²')
print('Digite abaixo os valores da altura e da largura em metros:')
altura = float(input('Altura em Metros: '))
largura = float(input('Largura em metros: '))
area_quadrada = altura*largura
tinta_necessaria = area_quadrada/2
print('A área total dessa parede é igual a {:.3f} M²'.format(area_quadrada), '\nSerão necessários {} litros de tinta para pintar toda a parede.'.format(tinta_necessaria))
