#-*-coding:utf8;-*-
#qpy:console

print('\n')
n = str(input('Digite um número de 0 a 9999: '))
print('\n')
print(' VALOR: {} \n UNIDADE: {} \n DEZENA: {} \n CENTENA: {} \n MILHAR: {}'.format(n, n[3:], n[2], n[1], n[0]))