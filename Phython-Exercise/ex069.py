homem = maior = menor = 0
while True:
    cont = 1
    print('-'*50)
    print(' '*15,'CADASTRE UMA PESSOA')
    print('-'*50)
    idade = 0
    while idade > 120:
        idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in ('FM'):
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print('-'*50)
    if idade > 18:
        maior +=1
    if sexo in 'M':
        homem +=1
    if sexo in 'F' and idade < 20:
        menor +=1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()
    if opcao in 'N':
        break    
print(f'\nTotal de pessoas cadastradas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {menor} mulheres com menos de 20 anos')
print('-'*50)