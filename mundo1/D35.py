#-*-coding:utf8;-*-
#qpy:console

print('\n')
print('-' * 5, 'ANÁLISE DE TRIÂNGULOS', '-' * 5)
print('\n')
a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = float(input('Digite o lado C do triângulo: '))
print('\n')
if a < b and a < c:
    if b < c:
        teste = a + b
        if teste > c:
            print('PODE SER FORMADO UM TRIÂNGULO')
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
    else:
        teste = a + c
        if teste > b:
            print('PODE SER FORMADO UM TRIÂNGULO')
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
elif b < a and b < c:
    if a < c:
        teste = b + a
        if teste > c:
            print('PODE SER FORMADO UM TRIÂNGULO')
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
    else:
        teste = b + c
        if teste > a:
            print('PODE SER FORMADO UM TRIÂNGULO')
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
elif c < a and c < b:
    if a < b:
        teste = c + a
        if teste > b:
            print('PODE SER FORMADO UM TRIÂNGULO')
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
    else:
        teste = c + b
        if teste > a:
            print('PODE SER FORMADO UM TRIÂNGULO')
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
else:
    print('\n')
    print('ERRO!')
