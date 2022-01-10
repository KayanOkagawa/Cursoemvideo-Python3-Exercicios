#-*-coding:utf8;-*-
#qpy:console

verde = '\033[32m'
roxo = '\033[35m'
nada = '\033[m'
print(verde, '-' * 5, nada, roxo, 'SOMA DE VALORES PARES', nada, verde, '-' * 5)
print('\n')
s = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
    else:
        s + 0
print('\n')
print('{} A Soma dos valores PARES é {}{}'.format(roxo, s, nada))