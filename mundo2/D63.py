#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;33m'
txt = '\033[33m'
nada = '\033[m'
count = 0
f1 = 0
f2 = 1
fn = 0

print('\n')

print(titulo, '-' * 8, 'Sequência de Fibonacci', '-' * 8, nada)

print('\n')

n = int(input('{}Digite a Quantidade de termos que você quer vê:{} '.format(txt, nada))) - 2
print('\n {}-{}'.format(f1, f2), end='-')
while  count < n:
        fn = f1 + f2
        f1 = f2
        f2 = fn
        print('{}'.format(fn), end='')
        count += 1
        print('-' if count < n else ' ', end='')
print('\n')     
