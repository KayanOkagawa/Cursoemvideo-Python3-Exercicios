#-*-coding:utf8;-*-
#qpy:console

vermelho = '\033[31m'
azul = '\033[34m'
nada = '\033[m'
print('\n')
print(vermelho, '-' * 5, 'CALCULADORA DE PA', '-' * 5, nada)
print('\n')
p1 = int(input('Digite o Primeiro termo da PA: '))
r = int(input('Digite a Razão da PA: '))
pa = [p1]
print('\n')
for c in range(0,9):
    resultado = pa[c] + r
    pa.append(resultado)   
print(azul, pa, nada)