print ('-'*50)
print(f'{" LISTAGEM DE PREÇOS ": ^50}')
print ('-'*50)
precos = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00)

for c in range(0,len(precos)):
    if c % 2 == 0:
        print(f'{precos[c]:.<40}R$',end='')
    else:
        print(f'{precos[c]:.2f}')
print ('-'*50)