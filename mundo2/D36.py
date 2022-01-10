#-*-coding:utf8;-*-
#qpy:console

import math,time

print('\n')
print('-' * 5, 'VERIFICADOR DE EMPRÉSTIMO', '-' * 5)
print('\n')
v = '\033[31m'
s = '\033[m'
casa = float(input('\033[33mDigite o Valor da Casa: R$ '))
salario = float(input('Digite o Valor do Salário: R$ '))
anos = int(input('Digite a Quantidade de Anos: '))
prestação = math.ceil(casa / (anos * 12))
print('\n')
print('CARREGANDO...\033[m')
time.sleep(3)
if prestação <= (salario * 0.30):
    print('\n')
    print(' Salário: R$ {}{}{} \n Valor da Casa: R$ {}{}{} \n Anos: {}{}{} \n Parcela: {}{}{}'.format(v, salario, s, v, casa, s, v, anos, s, v, prestação, s))
    print('\n')
    print('O Valor da sua parcela está no limite!')
else:
    print('\n')
    print(' Salário: R$ {}{}{} \n Valor da Casa: R$ {}{}{} \n Anos: {}{}{}'.format(v, salario, s, v, casa, s, v, anos, s, v, prestação, s))
    print('\n')
    print('O Valor da parcela não está no limite!')
