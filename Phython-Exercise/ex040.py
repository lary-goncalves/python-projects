print('\033[36m-*\033[m'*30)
print(' '*14,'\033[1mAvaliação de Média do Aluno\033[m')
print('\033[36m-*\033[m'*30)
nota1 = input('Primeira Nota: ')
nota2 = input('Segunda Nota: ')

try:
    nota1fl = float(nota1)
    nota2fl = float(nota2)
    media = (nota1fl + nota2fl) / 2
    print('A média do aluno é: \033[1m{}\033[m'.format(media))
    if media < 5:
        print('\nO aluno está \033[7;1;31mREPROVADO\033[m.')
    elif media >= 5 and media <= 6.9:
        print('\nO aluno está em \033[7;1;40;33mRECUPERAÇÃO\033[m.')
    elif media >= 7:
        print('\nO aluno está \033[1;7;32mAPROVADO\033[m.')
except ValueError:
    print('\n\033[1;7;31mDIGITE APENAS NÚMEROS\033[m')

print('\033[36m-*\033[m'*30)
