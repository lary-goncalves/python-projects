acum = media = val = cont = 0
while val == 0:
    maior = menor = num = (input('Digite um número: '))
    try:
        maior = menor = num = int(num)
        cont+=1
        acum+=num
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()
        while opcao not in 'SsNn':
            print('Opção Inválida')
            opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
        else:  
            while opcao == 'S' :
                    num = input('Digite um número: ')
                    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
                    val = 0
                    num = int(num)
                    cont+=1
                    acum+=num
                    if num < menor:
                        menor = num
                    elif num > maior:
                        maior = num
            if opcao == 'N':
                media = acum/cont
                print(f'Você digitou {cont} números e a média foi {media:.2f}\nO maior valor foi {maior} e o menor {menor}')
                val = 1
            else:
                break
    except ValueError:
        print('Opção inválida')
        val = 0
