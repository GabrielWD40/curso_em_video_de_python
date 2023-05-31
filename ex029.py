"""
Esse app deverá capturar a velocidade de um carro
Se ele estiver acima de 80 km por hora, deverá levar uma multa por cada km acima
Se não, nada acontece.
"""
print('Eis que você está com teu carrinho e BAM!! UM RADAR!!')
print('O limite de velocidade é 80 KM/H.')
velocidade = float(input('\nInforme a sua velocidade em KM: '))
if velocidade > 80:
    km_acima_da_media = (velocidade - 80)
    valor_multa = km_acima_da_media * 7
    print('Você está {}km acima do permitido, que é de 80km/h.'.format(km_acima_da_media))
    print('Por ser apressadinho, tome uma MULTA de R${}!'.format(valor_multa))
else:
    print("PARABÉNS POR ANDAR DENTRO DOS LIMITES DE VELOCIDADE.")