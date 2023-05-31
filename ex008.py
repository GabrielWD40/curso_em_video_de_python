#esse algoritmo deve ler um valor em metros e transformar para centímetros e milimetros.
print('Conversor de metros para centímetro e milímetro:')
metro = float(input('Digite uma metragem: '))
cent = metro*100
mili = metro*1000

print('*' * 50)
print('DE METROS PARA CENTÍMETRO E MILÍMETRO')
print("{} metros equivalem a {:.0f} centímetros!".format(metro, cent))
print("{} metros equivalem a {:.0f} milimetros".format(metro, mili))

print('*' * 50)
print('DE CENTÍMETRO PARA METRO E MILÍMETRO')
print("{:.0f} centímetros equivalem {} metros!".format(cent, cent/100))
print("{:.0f} centímetros equivalem a {:.0f} milimetros".format(cent, cent*10))

print('*' * 50)
print('DE MILÍMETRO PARA METRO E CENTÍMETRO')
print('{:.0f} milímetros equivalem a {} metros'.format(mili, mili/1000))
print('{:.0f} milímetros equivalem a {:.0f} centímetros'.format(mili, mili/10))
print('*' * 50)
