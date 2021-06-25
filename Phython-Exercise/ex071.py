print('='*50)
print('{: ^50}'.format(' BANCO LMG '))
print('='*50)
valor = int(input('Qual valor você quer sacar? R$ '))
c50 = c20 = c10 = c1 = 0
while True:
    while valor >= 50:
        valor-=50
        c50+=1
    while valor >=20:
        valor-=20
        c20+=1
    while valor >= 10:
        valor-=10
        c10+=1
    while valor >= 1:
        valor-=1
        c1+=1
    if valor == 0:
        break
print('='*50)
if c50 > 0:
    print (f'Total de {c50} cédulas R$ 50,00')
if c20 > 0:
    print (f'Total de {c20} cédulas R$ 20,00')
if c10 > 0:
    print (f'Total de {c10} cédulas R$ 10,00')
if c1 > 0:
    print (f'Total de {c1} cédulas R$ 1,00')
print('='*50)
print ('Volte Sempre ao Banco LMG! Tenha um bom dia!')
print('='*50)