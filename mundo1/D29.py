#-*-coding:utf8;-*-
#qpy:console

print('\n')
print('-' * 5, 'VERIFICADOR DE VELOCIDADE', '-' * 5)
print('\n')
v = int(input('Digite a velocidade do seu carro: '))
if v <= 80:
    print('Muito Bem! Você estava no limite de velocidade.')
else:
    multa = (v - 80) * 7
    print('Você estava a cima da velocidade! Será multado!')
    print('\n')
    print('Multa: R${:.2f}'.format(multa))
print('\n')
print('FIM!')