def notas(*nota, show=False):
    maior = menor = media = 0
    dados = dict()
    dados['total'] = len(nota)
    for n, c in enumerate(nota):
        if n == 0:
            maior = c
            menor = c
        elif c > maior:
            maior = c
        else:
            menor = c
    dados['maior'] = maior
    dados['menor'] = menor
    for n, c in enumerate(nota):
        media += c
    dados['media'] = media / len(nota)
    if show:
        if dados['media'] >= 7:
            dados['situação'] = 'MUITO BOA'
        elif 5 <= dados['media'] < 7:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados


resultado = notas(4.5, 9.5, 10, 6.5)
print('\n\033[01;32mANALISANDO ALUNOS\033[m')
print('-=' * 30)
print(resultado)
