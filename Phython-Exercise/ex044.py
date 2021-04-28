print('='*20,'LOJAS LÓGICA','='*20)

valorCompra = input('Preço das Compras: R$ ')
try:
    valorCompra = float(valorCompra)
    print('-' * 54)
    print('''FORMAS DE PAGAMENTO
[ 1 ] À vista - Dinheiro/Cheque
[ 2 ] À vista - Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x à 24x no Cartão''')
    print('-' * 54)

    pagamento = input('Qual é a opção? ').strip()

    try:
        pagamento = int(pagamento)
        if pagamento >= 1 and pagamento <5:
            print('-' * 54)
            if pagamento == 1:
                print('''Valor da Compra: R$ {:.2f} \nDesconto de 10% \nValor da Compra À vista - Dinheiro/Cheque: R$ {:.2f}'''.format(valorCompra, valorCompra - (valorCompra * 0.1)))
            elif pagamento == 2:
                print('''Valor da Compra: R$ {:.2f} \nDesconto de 5% \nValor da Compra À vista - Cartão: R$ {:.2f} '''.format(valorCompra, valorCompra - (valorCompra * 0.05)))
            elif pagamento == 3 or pagamento == 4:
                parcelas = input('Quantas parcelas? ').strip()
                try:
                    parcelas = int(parcelas)
                    validador = parcelas >= 1
                    if parcelas <= 2 and pagamento == 3:
                        valorParcela = valorCompra
                        print('''\nValor da Compra: R$ {:.2f} \nSua compra será parcelada em {}x SEM JUROS \nValor da Compra parcelada: R$ {:.2f}\nValor da Parcela: {}x de {:.2f}\n'''.format(
                                valorCompra, parcelas, valorParcela, parcelas, valorParcela / parcelas))
                    elif parcelas > 2 and parcelas < 24 and pagamento == 4:
                        valorParcela = (valorCompra*0.2)+valorCompra
                        print('''\nValor da Compra: R$ {:.2f} \nSua compra será parcelada em {}x \nValor da Compra parcelada: R$ {:.2f}\nValor da Parcela: {}x de {:.2f}\n'''.format(valorCompra,parcelas,valorParcela,parcelas,valorParcela/parcelas))
                    else:
                        print('-' * 54)
                        print('OPÇÃO INVÁLIDA')
                except ValueError:
                    print('-' * 54)
                    print('OPÇÃO INVÁLIDA')
        else:
            print('-' * 54)
            print('OPÇÃO INVÁLIDA')
    except ValueError:
        print('-' * 54)
        print('OPÇÃO INVÁLIDA')
except ValueError:
    print('-' * 54)
    print('OPÇÃO INVÁLIDA')
print('=' * 54)
