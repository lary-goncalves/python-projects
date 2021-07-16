palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for pos in palavras:
    palavra = pos
    print(f'\nNa palavra {pos} temos ',end='')
    for c in range (0,len(palavra)):
        if palavra[c] in 'AEIOU':
            print(f'{palavra[c].lower()}',end=' ')
