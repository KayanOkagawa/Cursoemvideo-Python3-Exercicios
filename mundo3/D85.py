titulo = '\033[01;33m'
txt = '\033[33m'
nada = '\033[m'
números = [[], []]

print(f'\n{titulo:-<14} Lista Composta Par e Impar {nada:->11}')

for c in range(0,7):
    num = int(input(f'\n{txt}Digite um número: {nada}'))
    if num % 2 == 0:
        números[0].append(num)
    else:
        números[1].append(num)
números[0].sort()
números[1].sort()
print(f'\n{txt}Lista Par: {números[0]}')
print(f'\nLista Impar: {números[1]}{nada}')