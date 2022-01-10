#-*-coding:utf8;-*-
#qpy:console

print('\n')
print('-' * 5, 'VERIFICADOR DE ANO BISSEXTOS', '-' * 5)
print('\n')
ano = int(input('Digite o ano: '))
etapa1 = ano % 4
etapa2 = ano % 400
print('\n')

if etapa1 == 0 or etapa2 == 0:
    print('O ano é BISSEXTO!')
else:
    print('Esse ano não é BISSEXTO!')
print('\n')
print('FIM!')
