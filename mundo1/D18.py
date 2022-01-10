#-*-coding:utf8;-*-
#qpy:console

from math import sin, cos, tan, radians
print('\n')
print('-' * 5, 'SENO, COSSENO E TANGENTE', 5 * '-')
print('\n')
ang = radians(float(input('Digite um ângulo: ')))
sen = sin(ang)
cos = cos(ang)
tan = tan(ang)
print(' Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(sen, cos, tan))
