#-*-coding:utf8;-*-
#qpy:console

print('\n')
print('-' * 5, 'AUMENTO NO SALÁRIO', '-' * 5)
print('\n')
s = float(input('Digite o seu salário: '))
if s > 1250:
    sr = (s * 0.10) + s
    print('\n')
    print(' SALÁRIO: {:.2f} \n AUMENTO: {:.2f} \n SALÁRIO REAJUSTADO: {:.2f}'.format(s, (s * 0.10), sr))
elif s <= 1250:
    sr = (s * 0.15) + s
    print('\n')
    print(' SALÁRIO: {:.2f} \n AUMENTO: {:.2f} \n SALÁRIO REAJUSTADO: {:.2f}'.format(s, (s * 0.15), sr))
else:
    print('\n')
    print('ERRO!')
