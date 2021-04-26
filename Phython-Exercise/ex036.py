#recebendo as informações
print('-='*50)
valor = float (input('\033[1;7;30mValor da casa:\033[m R$ '))
salario = float (input('\033[1;7;30mSalario do comprador:\033[m R$ '))
anos = float (input('\033[1;7;30mQuantos anos de financiamento?\033[m '))
print('-='*50)

#variáveis de calculo
prestacao = valor/(anos*12)
porcento = salario*0.3

#informando os dados inseridos
print('\nPara pagar uma casa de \033[1;43mR$ {:.2f} \033[m em \033[1;43m{:.0f} anos\033[m' .format(valor,anos),end='')
print(' a prestação será \033[1;43mR${:.2f}\033[m'.format(prestacao))

#validação de emprestimo
if prestacao < porcento:
    print('\033[1;42mEMPRÉSTIMO APROVADO!\033[m \U0001F604')
else:
    print('\033[1;41mEMPRESTIMO REPROVADO!\033[m \U0001F641')

#\U0001F641 - é o código para emoticon em UNICODE