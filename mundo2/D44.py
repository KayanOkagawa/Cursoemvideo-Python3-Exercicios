#-*-coding:utf8;-*-
#qpy:console

nada = '\033[m'
titulo = '\033[01;31m'
texto = '\033[33m'
print('\n', titulo, '-' * 5, 'Gerenciador de pagamentos ', '-' * 5, nada)
print(""" \n \033[33m(1) à vista dinheiro/cheque: 10% de desconto\n
(2) à vista no cartão: 5% de desconto\n
(3) em até 2x no cartão: preço normal \n
(4) 3x ou mais no cartão: 20% de juros""", '\n', '-' * 40, '\033[m')
produto = float(input('\033[31mDigite o valor da compra: \033[m'))
opcao = int(input('\n\033[31mDigite a forma de pagamento: \033[m'))
if opcao == 1:
    valor = produto - (produto * 0.10)
    print('\nValor: {}\nPagamento: Dinheiro/ Cheque'.format(valor))
elif opcao == 2:
    valor = produto - (produto * 0.05)
    print('\nValor: {}\nPagamento: Cartão Débito'.format(valor))
elif opcao == 3:
    vezes = int(input('\n\033[31mDigite a quantidade de parcelas: \033[m'))
    if vezes == 2 or vezes == 1:
        parcela = produto / vezes
        print('\nValor: {}\nPagamento: Cartão Crédito {}x\nParcelas: {}'.format(produto, vezes, parcela))
    else:
        print('Erro!')
elif opcao == 4:
    vezes = int(input('\n\033[31mDigite a quantidade de parcelas: \033[m'))
    if vezes <= 12:
        valor = produto + (produto * 0.2)
        parcela = produto / vezes
        print('\nValor: {}\nPagamento: Cartão Crédito {}x\nParcelas: {:.2f}'.format(valor, vezes, parcela))
    else:
        print('Erro!')