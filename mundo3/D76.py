produtos = ('Pão Francês', 11.58, 'Mortadela Perdigão', 6.34, 'Leite Jussara', 3.65, 'Banana', 4.56, 'Ovo', 8.75, 'Iorgute', 4.89)
nada = '\033[m'
titulo = '\033[01;34m'
txt = '\033[34m'
tamanho = float(len(produtos)) / 2

print(f'\n{titulo :-<20} LISTA DE PREÇOS {nada :->15}')

for count in range(0, int(tamanho)):
    if count == 0:
        print(f' \n {produtos[count]:.<30}  R$:{produtos[count+1]}\n')
    elif count != 0:
        print(f' {produtos[count * 2]:.<30}  R$:{produtos[(count * 2)+ 1]:}\n')
print(f'{titulo :-<50}{nada}')