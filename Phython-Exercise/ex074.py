from random import randint
numeros = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print(f'Os valores sorteados foram: {numeros[0]} {numeros[1]} {numeros[2]} {numeros[3]} {numeros[4]}')
print(f'O maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')
