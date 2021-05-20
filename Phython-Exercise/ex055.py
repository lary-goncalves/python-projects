peso = []

for p in range (1,6,1):
    pessoas = float (input('Digite o peso da {}ª pessoa: '.format(p)))
    peso.append(pessoas)

print('\nO maior peso lido foi de: {}'.format(max(peso)))
print('O menor peso lido foi de: {}'.format(min(peso)))
