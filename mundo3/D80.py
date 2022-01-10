titulo = '\033[01;36m'
txt = '\033[36m'
nada = '\033[m'
lista = list()
teste = False
ps = 1

print(f'\n{titulo:-<16} Lista ordenada sem Sort {nada:->12}')

for count in range(0,5):
    n = int(input(f'\n{txt}Digite um número: {nada}'))
    if count == 0:
        lista.append(n)
    else:
        for count in range(0, len(lista)):
            if n > lista[count]:
                ps += 1
            elif n < lista[count]:
                ps -= 1
                if ps < 0:
                    ps -= 1
                elif lista[ps] < n:
                    ps += 1
        lista.insert(ps, n)
        print(f'\n{txt}Valor adicionado na posição {lista.index(n)}ª da lista. {nada}')
        ps = 1
print(f'\n{titulo}Resultado: {lista}{nada}')