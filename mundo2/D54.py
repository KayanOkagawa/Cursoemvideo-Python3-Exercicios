#-*-coding:utf8;-*-
#qpy:console

import datetime
titulo = '\033[01;31m'
texto = '\033[34m'
nada = '\033[m'
atual = datetime.date.today().year
maioridade = []
menoridade = []
print('\n')
print(titulo, '-' * 8, 'Análise de Maioridade', '-' * 8, nada)
print('\n')
for c in range(1, 8):
    ano = int(input('{}Digite {}° ano de nascimento :{} '.format(texto, c, nada)))
    if atual - ano < 18:
        menoridade.append(ano)
    else:
        maioridade.append(ano)
print('\n Maioridade: {} Menoridade: {}'.format(len(maioridade), len(menoridade)))