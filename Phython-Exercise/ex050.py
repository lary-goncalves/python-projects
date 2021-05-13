soma = 0
for c in range (1,7):
    numero = int(input('Digite o {}º número: '.format(c)))
    if numero % 2 == 0:
        soma += numero
print('A soma dos números pares é: {}'.format(soma))
