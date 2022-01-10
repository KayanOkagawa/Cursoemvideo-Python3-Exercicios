#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;34m'
txt = '\033[34m'
nada = '\033[m'
count = 1
valor = 10
teste = 'S'

print('\n')
print(titulo, '-' * 5, 'PROGRESSÃO ARITMÉTICA', '-' * 5, nada)
print('\n')

razao = int(input('{}Digite a Razão da PA:{} '.format(txt, nada)))
primeirotermo = int(input('{}Digite o 1° termo da PA:{} '.format(txt, nada)))
pa = [primeirotermo]

print('\n')

while teste == 'S':
    while count < valor:
        pa.insert(count, pa[count - 1] + razao)
        count += 1
    print(pa)
    print('\n')
    teste = str(input('{}Gostaria de saber mais termos? [S/N]:{} '.format(txt, nada))).strip().upper()[0]
    if teste == 'S':
        n = int(input('{}Gostaria de ver mais quantos termos:{} '.format(txt, nada))) 
        valor = valor + n
        print('\n')
print('\nFIM')