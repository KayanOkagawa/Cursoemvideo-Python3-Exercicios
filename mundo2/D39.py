#-*-coding:utf8;-*-
#qpy:console

import datetime
print('-' * 5, 'ALISTAMENTO', '-' * 5)
print('\n')
anon = int(input('Digite o seu ano de nascimento: '))
anoa = datetime.date.today().year
idade = anoa - anon
print('\n')
if idade == 18:
    print('Você pode se alistar!')
elif idade < 18:
    tempo = 18 - idade
    print('Você não pode ser alistar!')
    print('Ainda no Prazo! Falta {} ano.'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Você já passou da idade!')
    print('Prazo expirado! Faz {} ano.'.format(tempo))
else:
    print('Erro!')
