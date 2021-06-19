from os import X_OK
from random import randint
print ('=-'*40)
print (25*' ','VAMOS JOGAR PAR OU IMPAR')
print ('=-'*40)
c = 0
while True:
    n = int (input('Diga um valor: '))
    pc = randint (1,10)
    resultado = n + pc
    opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print ('-'*80)
    print (f'Você digitou {n} e o computador {pc}. Total de {resultado}.')
    print ('-'*80)
    if resultado % 2 == 0 and opcao in 'Pp':
        print ('DEU PAR!\nVocê VENCEU!')
    elif resultado % 2 != 0 and opcao in 'Ii':
        print ('DEU IMPAR!\nVocê VENCEU')
    else:
        print ('Você PERDEU!')
        break
    print ('\nVamos jogar novamente...')
    print ('=-'*40)
    c += 1    
print ('=-'*40)
print (f'GAME OVER! Você venceu {c} vezes.')