frase = str(input('Digite uma frase: ')).strip().upper()
fraseInt = frase.replace(' ', '')
cont = 0
for c in range (0, len(fraseInt)):
    if fraseInt[c] == fraseInt[-c-1]:
        cont+=1
print('O inverso de {} é {}'.format(fraseInt,fraseInt[::-1]))
if cont == len(fraseInt):
    print('A frase digitada é Palindromo')
else:
    print('A frase digitada Não Palindromo')