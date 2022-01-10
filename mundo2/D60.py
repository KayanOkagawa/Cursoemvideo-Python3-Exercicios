#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;32m'
texto = '\033[33m'
nada = '\033[m'
fac = 1

print('\n')

print(titulo, '-' * 9, 'FATORAÇÃO DE NÚMEROS', '-' * 9, nada)

print('\n')

n = int(input('{}Digite o número para ser fatorado:{} '.format(texto, nada)))
count = n

print('\n')

print(' {}! ='.format(n), end=' ')

while count != 0:   
    if count > 1:
        print('{}'.format(count), end='x')
    else:
        print('{}'.format(count))
    fac *= count
    count -= 1
print('\n FATORAÇÃO = {}'.format(fac))