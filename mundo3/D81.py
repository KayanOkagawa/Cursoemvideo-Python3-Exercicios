titulo = '\033[01;35m'
txt = '\033[35m'
nada = '\033[m'
resposta = 'S'
lista = list()

print(f'\n{titulo:-<15} Análise de dados de uma Lista {nada:->7}')

while True:
    if resposta == 'S':
        lista.append(int(input(f'\n{txt}Digite um número: {nada}')))
        resposta = ' '
    while not resposta in 'SN':
        resposta = input(f'\n{txt}Deseja continuar ? [S/N]: {nada}').strip().upper()[0]
    if resposta == 'N':
        lista.sort(reverse=True)
        print(f'\n{titulo} Quantidade de valores digitado: {len(lista)} \n Lista em Ordem Inversa:', end = ' ')
        for c in lista:
            print(c, end=' ')
        if lista.count(5) >= 1:
            print(f'\nO Valor 5 foi digitado na posição: {lista.index(5)}{nada}')
        else:
            print(f'\n O Valor 5 não foi digitado {nada}')
        break