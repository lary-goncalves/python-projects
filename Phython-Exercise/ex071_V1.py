print('='*50)
print('{: ^50}'.format(' BANCO LMG '))
print('='*50)
valor = int(input('Qual valor você quer sacar? R$ '))
notas = 0
cedula = 50
while True:
    while valor >= cedula:
        valor-=cedula
        notas +=1 
    else:
        if notas > 0:
            print(f'Total de {notas} cédulas R${cedula},00')
            notas = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
    if valor == 0:
        break
print('='*50)
print ('Volte Sempre ao Banco LMG! Tenha um bom dia!')
print('='*50)