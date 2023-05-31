totaldenumerosdigitados = 0
somadosnumerosdigitados = 0
numero = int(input('Use 999 para parar\nDigite um número qualquer: '))
while numero != 999:
    somadosnumerosdigitados += numero
    totaldenumerosdigitados += 1
    numero = int(input('[Use 999 para parar]. Digite um outro número: '))
print('A soma dos {} valores que você digitou é = {}'.format(totaldenumerosdigitados, somadosnumerosdigitados))
