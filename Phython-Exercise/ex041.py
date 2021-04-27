#importando biblioteca de ano e pausa de apresentação
from datetime import date
from time import sleep

print('-*'*25)
print(' '*6,'CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-*'*25)
sleep(2)
print(''' As Categorias de Atletas são:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER''')
print('-*'*25)
sleep(3)
print('\nPara saber qual a sua Categoria')
nascimento = input('Digite o Ano de nascimento: ').strip()

try:
    nascimento = int(nascimento)
    idade = date.today().year - nascimento
    if idade <=120:
        print('\nO atleta tem {} anos'.format(idade))
        if idade <= 9:
            print('Classificação: MIRIM')
        elif 9 < idade <= 14:
            print('Classificação: INFANTIL')
        elif 14 < idade <= 19:
            print('Classificação: JÚNIOR')
        elif 19 < idade <=25:
            print('Classificação: SÊNIOR')
        elif 25 < idade <=120:
            print('Classificação: MASTER')
    else:
        print('\nClassificação NÃO EXISTENTE')
except ValueError:
    print('DIGITE UM ANO VÁLIDO')

print('')
print('-*'*25)