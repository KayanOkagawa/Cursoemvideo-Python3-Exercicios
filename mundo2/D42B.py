#-*-coding:utf8;-*-
#qpy:console
nada = '\033[m'
titulo = '\033[01;32m'
texto = '\033[01;35m'
print('\n')
print(titulo,'-' * 10, ' ANÁLISE DE TRIÂNGULO', '-' * 10, nada)
print('\n')
a = float(input('\033[35mDigite o valor do lado A: \033[m'))
b = float(input('\033[35mDigite o valor do lado B: \033[m'))
c = float(input('\033[35mDigite o valor do lado C: \033[m'))
print('\n')
if a+b >= c and b+c >= a and c+a >= b:
    print('Pode forma um triângulo!')
    if a == b and b == c:
        print(texto, '\n TIPO: Equilatero', nada)
    elif a != b and b != c:
        print(texto, '\n TIPO: Escaleno', nada)
    else:
        print(texto, '\n TIPO: Isósceles', nada)
else:
    print('Não é possível forma um triângulo')
