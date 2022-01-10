#-*-coding:utf8;-*-
#qpy:console

print('\n')
print('-' * 5, 'VERIFICADOR DE PAR OU IMPAR', '-' * 5)
print('\n')
n = int(input('Digite um número: '))
resultado = n % 2
print('\n')
if resultado == 0:
    print('O valor é PAR!')
else:
    print('O valor é IMPAR!')
print('\n')
print('FIM!')
