#-*-coding:utf8;-*-
#qpy:console

print('\n')
from math import trunc
print('-' * 5, 'PORÇÃO INTEIRA', '-' * 5)
print('\n')
n = float(input('Digite um Valor Real: '))
print('O valor real é {} e sua porção inteira é {}'.format(n, trunc(n)))
