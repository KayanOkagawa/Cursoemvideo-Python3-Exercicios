tupla = ('teclado', 'python', 'mouse', 'chinelo', 'cachorro', 'photoshop', 'naruto')
nada = '\033[m'
titulo = '\033[01;33m'
txt = '\033[33m'

print(f'\n{titulo :-<20} ANÁLISE DE VOGAIS {nada :->14}')

print(f'{txt}')
for count in tupla:
    palavra = count
    print(f'\n{palavra}', end=' ')
    for letra in palavra:
        if letra in 'aA':
            print('A', end = ' ')
        elif letra in 'eE':
            print('E', end = ' ')
        elif letra in 'iI':
            print('I', end = ' ')
        elif letra in 'oO':
            print('O', end = ' ')
        elif letra in 'uU':
            print('U', end = ' ')
    print ('\n')
print(f'{nada}')