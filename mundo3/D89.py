titulo = '\033[01;36m'
txt = '\033[37m'
nada = '\033[m'
alunos = list()
media = list()
dados = list()
resposta = 'S'
num = 0
print(f'\n{titulo:-<20} Análise de Média {nada:->15}')

while True:
    if resposta in 'S':
        nome = str(input(f'\n{txt}Digite o nome do aluno: {nada}')).capitalize()
        media.append(float(input(f'\n{txt}Digite a 1°Nota: {nada}')))
        media.append(float(input(f'\n{txt}Digite a 2°Nota: {nada}')))
        dados.append(nome)
        dados.append(media[:])
        alunos.append(dados[:])
        media.clear()
        dados.clear()
        resposta = ' '
    while not resposta in 'SN':
        resposta = str(input(f'\n{txt}Você deseja continuar ? [Sim/Não]: {nada}')).strip().upper()[0]
    if resposta in 'N':
        print(f"""\n{titulo}{'N°': ^10}    {'Nome': ^10}   {'Média': ^10}""")
        for posição, valor in enumerate(alunos):
            print(f"""\n{posição: ^10} {valor[0]: ^16} {(valor[1][0] + valor[1][1])/2: ^8}""")
        print('\n')
        while num != 999:
            num = int(input('\nDigite o número do aluno para saber a nota (999 desliga):'))
            if num != 999:
                print(f'\nO(a) {alunos[num][0]} tirou as notas {alunos[num][1]}')
        break