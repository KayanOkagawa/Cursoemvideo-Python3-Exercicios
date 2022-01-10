#-*-coding:utf8;-*-
#qpy:console

titulo = '\033[01;32m'
texto = '\033[33m'
nada = '\033[m'

print('\n', titulo, '-' * 10, 'Análise de Sexo', '-' * 10, nada, '\n')
sexo = ' '
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu Sexo[M/F]: ')).upper()[0].strip()
    print('\n')
    if sexo != 'M' and sexo != 'F':
        print('Erro! Valor digitado inválido. Tente novamente!')
        print('\n')
print('{}Análise concluída{}'.format(texto, nada))