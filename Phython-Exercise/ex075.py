a = int (input('Digite um número: '))
b = int (input('Digite outro número: '))
c = int (input('Digite mais um número: '))
d = int (input('Digite o último número: '))
numeros = (a, b, c, d)
print (f'\nVocê digitou os números {numeros}')
print (f'O numero 9 repetiu {numeros.count(9)} vezes')

try: 
    posição = numeros.index(3)
    print (f'O valor 3 apareceu na {numeros.index(3)}ª posição')
except ValueError:
    print('O número 3 não foi digitado')

print (f'Os valores pares foram ',end='')
for c in range(0,len(numeros)):
    if numeros[c] % 2 == 0:
        print(f'{numeros[c]} ',end='')
