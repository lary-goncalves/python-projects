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
            try: 
                opcao == 'N':
                media = acum/cont
                print('Você digitou {} números e a média foi {:.2f}\nO maior valor foi {} e o menor {}'.format(cont,media,maior,menor))
                val = 1
            except ValueError:
                print('Opção Inválida')
                
    except ValueError:
        print('Opção inválida')
        val = 0
        