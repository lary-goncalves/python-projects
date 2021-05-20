from datetime import date
contMenor = 0
contMaior = 0
for ano in range (1,8,1):
    idade = int (input('Em que ano a {}ª pessoa nasceu? '.format(ano)))
    if date.today().year - idade <18:
        contMenor+= 1
    else:
        contMaior+= 1

print ('Ao todo tivemos {} pessoas menores de idade'.format(contMenor))
print('E também tivemos {} pessoas maiores de idade'.format(contMaior))