#primeira solução
sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]# o zero é para pegar
cont = 1
while cont == 1:
    if sexo not in 'FfMm':
        sexo = input('Dados Inválidos. Por favor informe seu sexo: ').strip().upper()[0]
        cont = 1
    else:
        cont = 0
print('\nSexo {} registrado com sucesso'.format(sexo))


#segunda solução
# sexo = input('Informe seu sexo: [M/F] ')
# while sexo not in 'FfMm':
#     sexo = input('Dados Inválidos. Por favor informe seu sexo: ').upper()
# print('\nSexo {} registrado com sucesso'.format(sexo))
