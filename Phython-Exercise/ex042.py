print ('-='*30)
print (' '*15,'Analisador de Triângulos')
print ('-='*30)

r1 = input('Primeiro Segmento: ').strip()
r2 = input('Segundo Segmento: ').strip()
r3 = input('Terceiro Segmento: ').strip()

print('')

try:
    r1 = float(r1)
    r2 = float(r2)
    r3 = float(r3)
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
        if r1 == r2 == r3:
            print('Os segmentos acima pode formar um triângulo EQUILÁTERO')
        elif r1 != r2 != r3 != r1 :
            print('Os segmentos acima pode formar um triângulo ESCALENO')
        else:
            print('Os segmentos acima pode formar um triângulo ISÓSCELES')
    else:
        print('Os segmentos acima NÃO PODEM FORMAR triângulo')
except ValueError:
    print('\033[7;1;31mDIGITO INVÁLIDO\033[m')
print ('-='*30)