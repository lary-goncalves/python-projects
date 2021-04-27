print('\033[1;36m-=\033[m'*30)
print(' '*20,'\033[7;1;30mCalculadora de IMC\033[m')
print('\033[1;36m-=\033[m'*30)

kg = input('Qual é o seu peso? (Kg) ').strip()
altura = input('Qual é a sua altura? (m) ').strip()

try:
    kg = float(kg)
    altura = float(altura)
    imc = kg / (altura ** 2)
    print('\033[1;36m-=\033[m' * 30)
    print('O seu IMC é de {:.1f} kg/m²'.format(imc))
    if imc < 18.5:
        print('Você está \033[1;7;31mABAIXO DO PESO\033[m normal')
    elif 18.5 <= imc <= 25:
        print('Você está com o \033[1;7;32mPESO IDEAL\033[m')
    elif 25 < imc <= 30:
        print('Você está com \033[1;7;33;40mSOBREPESO\033[m')
    elif 30 < imc <= 40:
        print('Você está com \033[1;7;31mOBESIDADE\033[m')
    else:
        print('Você está em \033[1;7;31mOBESIDADE MÓRBIDA\033[m, cuidado!')

except ValueError:
    print('\n\033[1;7;31mA altura ou o peso está incorreto(a)\033[m')
print('\033[1;36m-=\033[m'*30)
