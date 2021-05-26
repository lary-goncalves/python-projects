from time import sleep
from random import randint

print('Olá, sou seu computador')
sleep(2)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(2)
print('Será que você consegue adivinhar qual foi?')
sleep(2)
palpite = int(input('Qual é o seu palpite?'))

pensamento = randint(0,10)
cont = 1
acum = 0

while cont == 1:
    acum += 1
    if palpite == pensamento:
        cont = 0
    elif palpite > pensamento:
        cont = 1
        palpite = int(input('Menos... Tente mais uma vez: '))
    elif palpite < pensamento:
        cont = 1
        palpite = int(input('Mais... Tente mais uma vez: '))
print(f'Acertou! Com {acum} tentativas. Parabéns!')
