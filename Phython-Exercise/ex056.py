totIdade = 0
compIdade = 0
maisVelho = ''
contF = 0

for p in range (1,5):
    print('-'*20,'{}ª pessoa'.format(p),'-'*20)
    nome = str (input('Nome: '))
    idade = int (input('Idade: '))
    sexo = str (input('Sexo [M/F]: ')).upper().strip()

    totIdade += idade
    if idade > compIdade:
        compIdade = idade
        maisVelho = nome
    if sexo == 'F' and idade < 20:
        contF+= 1

med = totIdade/4
print('-'*20)
print('\nA média de idade do grupo é de {}'.format(med))
print('O homem mais velho tem {} anos e se chama {}'.format(compIdade,maisVelho))

if contF > 1:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(contF))
elif contF == 0:
    print('Não há mulheres com menos de 20 anos')
else:
    print('Há apenas 1 mulher com menos de 20 anos')
