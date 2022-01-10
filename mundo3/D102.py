def fat(num, show=False):
    """
    FUNÇÃO DE FATORAÇÃO
    :param num: NUMERO QUE SERÁ FATORADO
    :param show: MOSTRA OU NÃO A CONTA
    :return: RETORNA O RESULTADO DA FATORAÇÃO
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
    return f


print(fat(5, show=True))
help(fat)
