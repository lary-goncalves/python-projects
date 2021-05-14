num = int(input('Digite um número: '))
cont = 0
for c in range (1,num+1,1):
    if num % c == 0:
        print ('\033[1;31m',c,'\033[m',end='')
        cont += 1
    else:
        print ('\033[1;33m',c,'\033[m',end='')
print('\n\nO número {} foi divisível {} vezes'.format(num,cont))
if cont <= 2:
    print('E por isso é PRIMO')
else:
    print('E por isso NÃO É PRIMO')