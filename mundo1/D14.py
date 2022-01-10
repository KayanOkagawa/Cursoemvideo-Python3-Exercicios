#-*-coding:utf8;-*-
#qpy:console

print(5 * '-', 'CONVERSOR DE TEMPERATURA', 5 * '-')
print('\n')
c = float(input('Digite o valor em Graus Celsius: '))
f = 1.8 * c + 32
print('O valor de {}°C em Farenheit é {}°F.'.format(c, f))
