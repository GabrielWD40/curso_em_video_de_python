# nesse algoritmo, devemos calcular a média das duas notas do aluno.
print('Vamos calcular a média do aluno Marcos:')
n1 = float(input('Digite a nota do 1º semestre: '))
n2 = float(input('Digite a nota do 2º semestre: '))
media = (n1 + n2) / 2

# as variáveis em python podem ter acentos

print('A média das notas de Marcos são: {:.2f}'.format(media))
print("É necessário ter a média maior do que 6 para passar.")
if media < 6:
    print('Ih Marcão, tu tá reprovado! Sua média foi de {:.2f}'.format(media))
else:
    print('Parabéns, Marcos! Sua média é {} e você foi aprovado.'.format(media))
