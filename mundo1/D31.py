#-*-coding:utf8;-*-
#qpy:console

print('\n')
print('-' * 5, 'VERIFICADOR DE VALOR', '-' * 5)
print('\n')
km = float(input('Digite a quantidade de KM: '))
print('\n')
if km <= 200:
    print('O valor da passagem sairá R$0.50 por KM.')
    print('\n')
    valor = km * 0.50
    print('Valor: R${:.2f}'.format(valor))
else:
    print('O valor da passagem sairá R$0.45 por KM.')
    print('\n')
    valor = km * 0.45
    print('Valor: R${:.2f}'.format(valor))
print('\n')
print('FIM!')
