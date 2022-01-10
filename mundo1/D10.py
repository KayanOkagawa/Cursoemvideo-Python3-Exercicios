#-*-coding:utf8;-*-
#qpy:console

print(5 * '-', 'CONVERSOR DE MOEDAS', 5 * '-')
print('\n')
r = float(input('DIGITE O VALOR EM REAIS: '))
d = r / 5.29
e = r / 6.41
print('\n')
print(' CONVERSÃO - USS: {:.2f} / EURO: {:.2f}'.format(d, e))
