c = 0
cont = 0
soma = 0
for c in range (c % 3,501,3):
    if not c % 2 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))
