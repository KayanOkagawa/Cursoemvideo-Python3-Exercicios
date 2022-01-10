dados = dict()
gols = list()

print('\n\033[01;32mANALISE DE JOGADOR\033[m')
print('-=' * 30)

dados['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Digite a quantidade de partidas: '))

for c in range(0, partidas):
    gols.append(int(input(f'Na partida {c+1}, ele marcou: ')))

dados['gols'] = gols[:]
dados['total'] = sum(gols)


print('\n\033[01;32mDADOS DO JOGADOR\033[m')
print('-=' * 30)

for k, v in dados.items():
    print(f'{k.upper()}: {v}')

print('\n\033[01;32mTABELA DO CAMPEONATO\033[m')
print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for c in range(0, len(dados['gols'])):
    print(f'-> Na partida {c+1}, ele fez {dados["gols"][c]}')