total = cont = menor = 0
NomeMenor = ' '
print('-'*50)
print(' '*15,'LOJA SUPER BARATÃO')
print('-'*50)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    if menor == 0 and NomeMenor == ' 'or preco < menor:
        menor = preco
        NomeMenor = produto
    if preco > 1000:
        cont +=1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
print('-'*17,'FIM DO PROGRAMA','-'*17)
print(f'\nO valor total da compra foi de {total}')
if cont > 1:
    print(f'Temos {cont} produtos custando mais de R$1000,00')
else:
    print(f'Temos 1 produto custando mais de R$1000,00')
print(f'O produto mais barato foi {NomeMenor} que custa {menor:.2f}')
print('-'*50)