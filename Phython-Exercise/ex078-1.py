valores = []
posmax = []
posmin = []

for cont in range(0,5):
    valores.append(int(input(f'Digite um número na posição {cont}: ')))
print(f'Você digitou os valores {valores}')

for c,p in enumerate(valores):  
    if max(valores) == p:
        posmax.append(c)
    if min(valores) == p:
        posmin.append(c)

print(f'O maior valor digitado foi {max(valores)} nas posições {posmax}')
print(f'O menor valor digitado foi {min(valores)} nas posições {posmin}')
