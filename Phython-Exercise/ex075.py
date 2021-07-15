numeros = (int (input('Digite um número: ')), int (input('Digite outro número: ')), int (input('Digite mais um número: ')), int (input('Digite o último número: ')))
print (f'\nVocê digitou os números {numeros}')
print (f'O numero 9 repetiu {numeros.count(9)} vezes')

try: 
    3 in numeros
    print (f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
except ValueError:
    print('O número 3 não foi digitado')

print (f'Os valores pares foram ',end='')

for c in range(0,len(numeros)):
    if numeros[c] % 2 == 0:
        print(f'{numeros[c]} ',end='')
