while True:
    c = 0
    n = int (input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if n < 0:
        break
    while c < 10:
        c+=1
        print(f'{n} x {c} = {n*c}')
    print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')