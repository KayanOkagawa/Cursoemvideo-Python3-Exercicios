print('\n\033[01;35mFICHA DO JOGADOR\033[m')
print('-=' * 30)


def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    return nome, gols


nome_jogador = str(input('Nome do Jogador: '))
gols_jogador = str(input('Número de Gols: '))
resp = ficha(nome_jogador, gols_jogador)
print('-=' * 30)
print(f'\033[07;35mO jogador {resp[0]} fez {resp[1]} gols(s) no campeonato.\033[m')
