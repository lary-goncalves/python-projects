from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print(f'{" JOGO JOKENPÔ! ":=^60}')
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input('Qual é a sua jogada? '))

print('-='*30)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*30)

print('Computador: {}'.format(itens[computador]))
print('Jogador: {}'.format(itens[jogada]))

if computador == jogada:
    print('EMPATE!')
elif computador == 0 and jogada == 2 or computador == 1 and jogada == 0 or computador == 2 and jogada == 1:
    print('COMPUTADOR GANHOU!')
elif jogada == 0 and computador == 2 or jogada == 1 and computador == 0 or jogada == 2 and computador == 1:
    print('VOCÊ GANHOU!')
else:
    print('TENTATIVA INVÁLIDA!')

print('='*60)