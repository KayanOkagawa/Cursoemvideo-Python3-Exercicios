#-*-coding:utf8;-*-
#qpy:console

print(5 * '-','REAJUSTE SALARIAL', 5 * '-')
print('\n')
s = float(input('DIGITE O SEU SALÁRIO: '))
sa = s + (s * 0.15)
print('\n')
print('SALARIO REAJUSTADO: {:.2f}'.format(sa))
