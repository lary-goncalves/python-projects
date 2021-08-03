valores = []
for cont in range(0,5):
    valores.append(int(input(f'Digite um número na posição {cont}: ')))

print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for cont in range(0,5):  
    if max(valores) == valores[cont]:
        print (cont,end='... ')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for cont in range(0,5):  
    if min(valores) == valores[cont]:
        print (cont,end='... ')