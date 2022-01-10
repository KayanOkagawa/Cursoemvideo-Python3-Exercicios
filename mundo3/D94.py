print('\n\033[01;36mCADASTRO DE DADOS\033[m')
print('-=' * 30)

pessoas = list()
dados = dict()
resp = 'S'
media = 0

while True:
    if resp in 'S':
        dados['nome'] = input('Digite o seu nome: ')
        dados['idade'] = int(input('Digite a sua idade: '))
        dados['sexo'] = input('Digite o seu sexo[M/F]: ').strip().upper()[0]
        media += dados['idade']
        pessoas.append(dados.copy())
        dados.clear()
        resp = ''
        print('-=' * 30)
    while True:
        resp = input('Deseja continuar [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            print('-=' * 30)
            break
    if resp in 'N':
        print('\033[01;36mDADOS GERADOS\033[m')
        print(f'\nQUANTIDADE DE CADASTROS: {len(pessoas)}')
        print(f'MEDIA DAS IDADES: {media/len(pessoas):.1f}')
        print('PESSSOAS DO SEXO (F): ', end=' ')
        for c in pessoas:
            if c['sexo'] == 'F':
                print(c['nome'], end=' ')
        print('\nPESSOAS ACIMA DA MEDIA:', end=' ')
        for c in pessoas:
            if c['idade'] > media/len(pessoas):
                print(c['nome'], end=' ')
        print('<ENCERRADO>')
        break
