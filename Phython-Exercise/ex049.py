numero = int(input('Digite um número para ver sua tabuada: '))
for c in range (1,11,1):
    print('{} x {:2} = {:2}'.format(numero,c,(numero*c)))
