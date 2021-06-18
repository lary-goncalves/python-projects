n = s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        opcao = input('Deseja parar? [S/N]').strip().upper()
        if opcao == 'S':
            break
        elif opcao == 'N':
            n = 0 
            c-=1      
    c+=1
    s+=n 
print(f'A soma dos {c} é {s}')