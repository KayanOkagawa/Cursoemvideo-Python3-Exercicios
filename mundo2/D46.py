#-*-coding:utf8;-*-
#qpy:console

import time
vermelho = '\033[31m'
amarelo = '\033[33m'
nada = '\033[m'
print(vermelho, '-' * 5, ' CONTAGEM REGRESSIVA ', '-' * 5, nada)
print('\n')
for c in range(10, 0, -1):
    print(amarelo, c, nada)
    time.sleep(1)
print('\n')
print('*FOGOS DE ARTIFÍCIOS*')
