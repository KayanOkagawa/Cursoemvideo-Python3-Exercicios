#-*-coding:utf8;-*-
#qpy:console

print(5 * '-', 'ALUGUEL DE CARROS', 5 * '-')
print('\n')
d = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de KM: '))
a = (d * 60) + (km + 0.15)
print('ALUGUEL: R${}'.format(a))