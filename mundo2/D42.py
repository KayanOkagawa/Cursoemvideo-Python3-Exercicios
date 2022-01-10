#-*-coding:utf8;-*-
#qpy:console

#-*-coding:utf8;-*-
#qpy:console

print('\n')
print('-' * 5, 'ANÁLISE DE TRIÂNGULOS', '-' * 5)
print('\n')
a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = float(input('Digite o lado C do triângulo: '))
print('\n')
def equilátero (l1, l2, l3):
    if l1 == l2 and l2 == l3:
        print('TIPO: Equilátero')
def isósceles (l1, l2, l3):
    if l1 == l2 and l2 != l3 or l3 == l1 and l1 != l2 or l2 == l3 and l3 != l1:
        print('TIPO: Isósceles')
def escaleno (l1, l2, l3):
    if l1 != l2 and l2 != l3 and l3 != l1:
        print('TIPO: Escaleno')
if a < b and a < c:
    if b < c:
        teste = a + b
        if teste > c:           
            print('PODE SER FORMADO UM TRIÂNGULO')
            isósceles (a, b, c)
            escaleno (a, b, c)         
        elif teste < c:
            print('NÃO PODE SER UM TRIÂNGULO')
    elif not b < c:
        teste = a + c
        if teste > b:
            print('PODE SER FORMADO UM TRIÂNGULO')
            isósceles (a, b, c)
            escaleno (a, b, c)
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
elif b < a and b < c:
    if a < c:
        teste = b + a
        if teste > c:
            print('PODE SER FORMADO UM TRIÂNGULO')
            isósceles (a, b, c)
            escaleno (a, b, c)
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
    elif not a < c:
        teste = b + c
        if teste > a:
            print('PODE SER FORMADO UM TRIÂNGULO')
            isósceles (a, b, c)
            escaleno (a, b, c)
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
elif c < a and c < b:
    if a < b:
        teste = c + a
        if teste > b:
            print('PODE SER FORMADO UM TRIÂNGULO')
            isósceles (a, b, c)
            escaleno (a, b, c)
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
    elif not a < b:
        teste = c + b
        if teste > a:
            print('PODE SER FORMADO UM TRIÂNGULO')
            isósceles (a, b, c)
            escaleno (a, b, c)
        else:
            print('NÃO PODE SER UM TRIÂNGULO')
else:
    print('\n')
    print('PODE SER FORMADO UM TRIÂNGULO!')
    equilátero (a, b, c)
    isósceles (a, b, c)
    escaleno (a, b, c)
