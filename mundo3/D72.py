números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
titulo = '\033[01;34m'
txt = '\033[34m'
nada = '\033[m'

print('\n')

print(f'{titulo:-<17} ANÁLISE DE NÚMERO EXT {nada:->13}')

esc = int(input(f'\n {txt}Digite um número entre 0 e 20: {nada}'))

if esc < 0 or esc > 20:
    while esc > 20 or esc < 0:
        esc = int(input(f'\n {txt}Digite um número entre 0 e 20: {nada}'))
print(f'\n {txt}Você digitou o número {números [esc]}{nada}')