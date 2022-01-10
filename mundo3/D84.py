titulo = '\033[01;34m'
txt = '\033[34m'
nada = '\033[m'
pessoas = list()
dados = list()
resposta = 'S'

print(f'\n{titulo:-<20} Análise de Peso {nada:->16}')
while True:
    if resposta in 'S':
        dados.append(str(input(f'\n{txt}\nDigite o seu nome: {nada}')))
        dados.append(float(input(f'\n{txt}\nDigite o seu peso: {nada}')))
        pessoas.append(dados[:])
        dados.clear()
        if len(pessoas)-1 == 0:
           menor = maior = pessoas[0][1]
        else:
            for c in pessoas:
                if c[1] > maior:
                    maior = c[1]
                elif c[1] < menor:
                    menor = c[1]
        resposta = ' '
    while not resposta in 'SN':
        resposta = str(input(f'{txt}\nVocê deseja continua ? [S/N]: {nada}')).strip().upper()[0]
    if resposta in 'N':
        print(f'{titulo}\nForam Cadastradas: {len(pessoas)}{nada}')
        print(f'{titulo}\nO maior peso foi {maior}. Peso de', end=' ')
        for c in pessoas:
            if maior == c[1]:
                print(c[0], end='...')
        print(f'{titulo}\nO menor peso foi {menor}. Peso de', end=' ')
        for c in pessoas:
            if menor == c[1]:
                print(c[0], end='...')
        break