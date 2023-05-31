#esse algoritmo deve calcular o valor que uma poessoa deve pagar num carro alugado.
#lembrando que a diária custa 60 pila
#a cada KM rodado é cobrado 15 centavos

print('Calculadora de aluguel de carro.')
diária = int(input('Você usou o carro por quantos dias? \n'))
quilometragem = float(input('Você rodou quantos quilômetros? \n'))
aluguel = ((diária*60) + (0.15*quilometragem))

print('\nVocê deverá pagar R${:.2f} à locadora de veículos que te alugou o veículo.'.format(aluguel))