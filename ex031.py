"""
Esse algoritmo deve calcular o valor de uma passagem com base na distância digitada pelo usuário.
Cobre 0,50 por km para viagens até 200km
Cobre 0,45 por km rodado para viagens acima de 200km
"""

print('Vamos calcular o valor das suas passagens de viagem.')
print('Para distâncias até 200km você R$0,5 centavos por KM rodado.\nPara distâncias acima 200km você R$0,45 centavos por KM rodado.')
distancia_da_viagem = float(input('\nDigite a distância em KM do seu ponto de partida até o ponto de chegada: '))
if distancia_da_viagem <= 200:
    print('Sua viagem é abaixo de 200km, você pagará o valor integral da passagem.')
    valor_ate_200km = distancia_da_viagem * 0.5
    print('O valor que você terá de desenbolsar é de R${:.2f} reais!'.format(valor_ate_200km))
else:
    print('Sua viagem é acima de 200km, você terá um pequeno desconto.')
    valor_acima_de_200km = distancia_da_viagem * 0.45
    print('O valor que você terá de desenbolsar é de R${:.2f} reais!'.format(valor_acima_de_200km))