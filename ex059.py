from time import sleep
op = 4
while op == 4:
    n1 = int( input('Primeiro número: '))
    n2 = int( input('Segundo número: '))
    op = 0
    while op == 0:
        sleep(1)
        print('''=-==-==-==-==-==-==-==-==-==-==-==-==
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair''')
        print('=-==-==-==-==-==-==-==-==-==-==-==-==')
        op = int (input('Opção: '))
        if op == 5:
            print('\nFINALIZANDO...')
        elif op > 5:
            print('\nOpção INVÁLIDA!')
            op = 0
        while op == 1:
            soma = n1 + n2
            print (f'A soma entre {n1} e {n2} é: {soma} ')
            op = 0
        while op == 2:
            multi = n1 * n2
            print (f'A multiplicação de {n1} e {n2} é: {multi}')
            op = 0
        while op == 3:
            if n1 > n2:
                print(f'O maior número entre {n1} e {n2} é: {n1}')
                op = 0
            else:
                print (f'O maior número entre {n1} e {n2} é: {n2}')
                op = 0
