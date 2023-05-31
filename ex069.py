
print('Cadastrando usuários')
numero_de_masculino = numero_de_feminino = maiores_de_idade = mulheres_menores_de_20anos = 0
while True:
    gênero = str(input('\nQual o gênero do indivíduo?'
                       '\n Use "M" para masculino'
                       '\n Use "F" para feminino'
                       '\n Gênero: ')).lower().strip()[0]
    while gênero[0] != 'm' and gênero[0] != 'f':
        print('\nOPÇÃO INVÁLIDA!!')
        gênero = str(input('Use "M" para masculino e "F" para feminino!'
                           '\n Gênero: ')).lower().strip()[0]
    if gênero == 'm':
        numero_de_masculino += 1
    elif gênero == 'f':
        numero_de_feminino += 1
    idade = int(input(f'Qual a idade da pessoa? '))
    if idade >= 18:
        maiores_de_idade += 1
    if idade < 20 and gênero == 'f':
        mulheres_menores_de_20anos += 1

    escolha = str(input('\nVocê deseja cadastrar mais alguém? (S / N) ')).upper().strip()
    while escolha[0] != 'S' and escolha[0] != 'N':
        escolha = str(input('Você deseja cadastrar mais alguém? (S / N) ')).upper().strip()
    if escolha[0] == 'N':
        break
    print('=' * 50)
print('=' * 50)
print(f'\nNo seu cadastro existem {maiores_de_idade} pessoas com 18 ou mais.')
print(f'Foram cadastrados {numero_de_masculino} homens no total!')
print(f'Foram cadastrados {numero_de_feminino} mulheres no total!')
print(f'Das {numero_de_feminino} mulheres, {mulheres_menores_de_20anos} tem menos de 20 anos de idade.')