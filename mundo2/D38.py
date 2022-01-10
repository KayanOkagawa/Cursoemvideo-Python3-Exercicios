#-*-coding:utf8;-*-
#qpy:console

print('-' * 5, 'MAIOR OU MENOR', 5 * '-')
print('\n')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
print('\n')
if n1 > n2:
    print('O Primeiro Valor é maior!')
elif n2 < n1:
    print('O Segundo Valor é maior!')
elif n1 == n2:
    print('Os Valores são iguais!')
else:
    print('Erro!')
