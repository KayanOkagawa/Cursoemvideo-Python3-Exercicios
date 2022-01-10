titulo = '\033[01;36m'
txt = '\033[36m'
nada = '\033[m'
count = 1
print('\n')
print(titulo, '-' * 9, 'PROGRESSÃO ARITMÉTICA', '-' * 9, nada)
print('\n')
razao = int(input('{}Digite a Razão da PA:{} '.format(txt, nada)))
primeirotermo = int(input('{}Digite o 1° termo da PA:{} '.format(txt, nada)))
pa = [primeirotermo]
print('\n')
while count < 10:
    pa.insert(count, pa[count - 1] + razao)
    count += 1
print(titulo, pa, nada)
        