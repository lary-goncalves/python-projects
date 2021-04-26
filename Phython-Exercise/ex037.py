#recebendo o número
numero = int(input('\033[1;36mDigite um número: \033[m'))

#menu de escolha
print('Escolha uma das bases numéricas para conversão:')
print('\033[36m-=\033[m'*30)
print('''\033[7;30m[ 1 ]\033[m Converter para \033[1;7;36mBINÁRIO\033[m 
\033[7;30m[ 2 ]\033[m Converter para \033[1;7;36mOCTAL\033[m 
\033[7;30m[ 3 ]\033[m Converter para \033[1;7;36mHEXADECIMAL\033[m''')
print('\033[36m-=\033[m'*30)
menu = int (input('Sua escolha: '))


#criando as condições
if menu == 1:
    print('\033[1;32m{}\033[m convertido para \033[1;7;37mBINÁRIO\033[m é igual a \033[1;32m{}\033[m'.format(numero,bin(numero)[2:]))
elif menu == 2:
    print('\033[1;32m{}\033[m convertido para \033[1;7;37mOCTAL\033[m é igual a \033[1;32m{}\033[m'.format(numero,oct(numero)[2:]))
elif menu == 3:
    print('\033[1;32m{}\033[m convertido para \033[1;7;37mHEXADECIMAL\033[m é igual a \033[1;32m{}\033[m'.format(numero,hex(numero)[2:]))
else:
    print('\033[1;7;31mOpção Inválida! Tente novamente!\33[m')