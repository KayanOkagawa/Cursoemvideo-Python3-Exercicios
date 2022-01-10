print('\n\033[01;31mANALISE DE JOGADOR COM REGISTRO DE DADOS\033[m')
print('-=' * 30)

jogadores = list()
dados = dict()
gols = list()
resp = 'S'

while True:
    if resp in 'S':
        dados['nome'] = str(input('Digite o nome do jogador: '))
        partidas = int(input(f'Digite quantas partidas, {dados["nome"]} jogou: '))
        for p in range(0, partidas):
            gols.append(int(input(f'Na partida {p+1}, quantos gols foram marcados: ')))
        dados['gols'] = gols[:]
        dados['total'] = sum(dados['gols'])
        jogadores.append(dados.copy())
        dados.clear()
        resp = ''
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            print('-=' * 30)
            break
    if resp in 'N':
        print('\033[01;31mDADOS REGISTRADOS\033[m')
        print('-=' * 30)
        print(f'{"COD.": <5}', end=' ')
        print(f'{"NOME:": <10}', end=' ')
        print(f'{"GOLS:": <15}', end=' ')
        print(f'{"TOTAL:":}')
        for c in range(0, len(jogadores)):
            print(f'{c: <5}', end=' ')
            for v in jogadores[c].values():
                if type(v) is list:
                    print(f'{v}', end='')
                else:
                    if type(v) is int:
                        print(f'{v: >10}', end='')
                    else:
                        print(f'{v: <10}', end='')
            print('\n')
        while True:
            valor = int(input('\033[01;36mGostaria de ver qual jogador?[COD./999 - desliga]:\033[m '))
            if valor == 999:
                break
            elif valor > len(jogadores)-1:
                print('ERRO! Digite um codigo valido')
            else:
                print(jogadores[valor])
        break

