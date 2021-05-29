num = int(input('Digite um número para calcular seu fatorial: '))
fat = num
cont = num + 1
print(f'Calculando {num}! = {num} ', end = '')
while cont != 0:
    cont -= 1
    if cont - 1 != 0 and cont !=0:
        print('X',cont - 1, end=' ')
        fat *= cont-1
print('=',fat)