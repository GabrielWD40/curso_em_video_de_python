nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))
genero = str(input('Digite o seu gênero (M/F): ')).lower()
lista = ['m', 'f', 'masculino', 'feminino', 'homem', 'mulher']
# Sempre que você precisar que uma variável seja nula, use o 'None'.
while genero not in lista:
    genero = str(input('Por favor, digite uma opção válida! (M/F): ')).lower().strip()
print()

if genero == 'f' or genero == 'feminino' or genero == 'mulher':
    genero_formatado = 'Feminino'
    print('Seus dados foram enviados com sucesso!')
    print('Nome: {}\n'
          'Idade: {}\n'
          'Gênero: {}'.format(nome, idade, genero_formatado))

elif genero == 'm' or genero == 'masculino' or genero == 'homem':
    genero_formatado = 'Masculino'
    print('Seus dados foram enviados com sucesso!')
    print('Nome: {}\n'
          'Idade: {}\n'
          'Gênero: {}'.format(nome, idade, genero_formatado))
