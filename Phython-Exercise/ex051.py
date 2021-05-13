print('='*60)
print(f'{" 10 TERMOS DE UMA PA ": ^60}')
print('='*60)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao #formula para calcular o enesimo numero de uma PA
for c in range (termo, decimo + razao , razao):
    print(c, end=' \U000027AA ')
print('ACABOU')
print('='*60)
