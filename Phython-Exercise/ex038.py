#recebendo os número
print('\033[1;33m-=\033[m'*30)
primeiro = input('\033[1;7;30mPrimeiro Número:\033[m ')
segundo = input('\033[1;7;30mSegundo Número:\033[m ')
print('\033[1;33m-=\033[m'*30)

#validando se é número
if primeiro.isnumeric() and segundo.isnumeric():
    primeiro = int(primeiro)
    segundo = int (segundo)
    #validando se o primeiro ou o segundo é maior ou igual
    if primeiro > segundo:
        print('O \033[1;7;32mPRIMEIRO\033[m número é maior')
    elif segundo > primeiro:
        print('O \033[1;7;32mSEGUNDO\033[m número é maior')
    else:
        print('Os valores são \033[32;7;1mIGUAIS\033[m')
#
else:
    print('\033[1;7;31mDigite um número inteiro positivo\033[m')
