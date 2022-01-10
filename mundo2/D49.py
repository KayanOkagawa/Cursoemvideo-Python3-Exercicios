#-*-coding:utf8;-*-
#qpy:console

print('-' * 5, ' TABUADAS AUTOMÁTICAS ', '-' * 5)
print('\n')
n = int(input('Digite um número: '))
print('\n')
for c in range(0, 11):
    v = n * c
    print('{} x {} = {}'.format(n, c, v))
