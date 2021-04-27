#importando biblioteca de data
from datetime import date

#titulo do programa
print('-='*30)
print(' '*17,'\033[1;7;30mValidador de Alistamento\033[m')
print('-='*30)

#recebendo GENERO
print('''Qual é o seu genero?
[F] Feminino 
[M] Masculino''')
genero = str(input('\nSua escolha: ')).upper().strip()

#Em caso de masculino, recebe ano de nascimento
if genero == 'M':
    print(('-=' * 30))
    nascimento = int(input('Ano de Nascimento: '))
    idade = date.today().year - nascimento
    maior = 18
    #validação se nascimento é superior ao ano atual e inferior ao ano de início da obrigatoriedade de alistamento
    if nascimento <= date.today().year and nascimento >= 1993 :
        print('\nQuem nasceu em {} tem {} anos em {}'.format(nascimento, idade, date.today().year))
        #validação de quem passou do prazo de alistamento
        if idade > maior:
            anosAlistamento = idade - maior
            print('\nVocê deveria ter se alistado há \033[1;31m{} anos\033[m'.format(anosAlistamento))
            print('Seu alistamento foi em \033[7;1;31m{}\033[m'.format(date.today().year - anosAlistamento))
        #validação de quem ainda vai se alistar
        elif idade < maior:
            anosAlistamento = maior - idade
            print('\nAinda faltam \033[1;32m{} anos\033[m para você se alistar'.format(anosAlistamento))
            print('Seu alistamento será em \033[7;1;32m{}\033[m'.format(date.today().year + anosAlistamento))
        #validação de quem está no ano de alistamento
        else:
            print('\n\033[1mVocê deve se alistar \033[7;1;33;40mIMEDIATAMENTE!\033[m')
    #informativo de qual seria o ano de obrigatoriedade de alistamento antes da lei em 2011
    elif nascimento<1993 and nascimento>1500:
        anosAlistamento = nascimento + maior
        if anosAlistamento < 2011:
            print('-=' * 30)
            print('Em \033[1;7;30m{}\033[m seu alistamento não era obrigatório'.format(anosAlistamento))
    # alerta de ano inferior ao ano de descobrimento do brasil
    else:
        print('-=' * 30)
        print('\033[7;1;40;31mO ano digitado não é válido\033[m')
#Retorno de alistamento não obrigatório para mulher
elif genero == 'F':
    print('-=' * 30)
    print('\033[1;7;30mSeu alistamento não é obrigatório\033[m ')
#Quando selecionada opção diferente de F ou M
else:
    print('-=' * 30)
    print('\033[1;7;31mOpção Inexistente\033[m')

print('-='*30)
