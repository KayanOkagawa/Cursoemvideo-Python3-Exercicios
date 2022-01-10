#-*-coding:utf8;-*-
#qpy:console

print('-' * 5, ' SOMA DE NÚMEROS ÍMPARES ', '-' * 5)
print('\n')
s = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        s += n
print('VALOR FINAL: {}'.format(s))
