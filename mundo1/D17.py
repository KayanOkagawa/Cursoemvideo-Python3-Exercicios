#-*-coding:utf8;-*-
#qpy:console
print('\n')
from math import hypot
print('-' * 5, 'HIPOTENUSA DE TRIÂNGULO RETÂNGULO', 5 * '-')
print('\n')
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('\n')
print(' Cateto Oposto: {} \n Cateto Adjacente: {} \n Hipotenusa: {:.2f}'.format(co, ca, h))
