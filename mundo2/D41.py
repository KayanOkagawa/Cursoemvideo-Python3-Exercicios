#-*-coding:utf8;-*-
#qpy:console

import datetime
atual = datetime.date.today().year
amarelo = '\033[33m'
ciano = '\033[36m'
nada = '\033[m'
print(amarelo, '-' * 10, nada, ciano, 'CATEGORIA NATAÇÃO' , nada, amarelo, '-' * 10, nada)
print('\n')
nascimento = int (input ('\033[33mDigite o ano de nascimento: \033[m'))
idade = atual - nascimento
print('\n')
if idade <= 9:
    print(amarelo, 'CATEGORIA: MIRIM', nada)
elif idade > 9 and idade <= 14:
    print(amarelo, 'CATEGORIA: INFANTIL', nada)
elif idade > 14 and idade <= 19:
    print(amarelo, 'CATEGORIA: JUNIOR', nada)
elif idade == 20:
    print(amarelo, 'CATEGORIA: SÊNIOR', nada)
elif idade > 20:
    print(amarelo, 'CATEGORIA: MASTER', nada)
