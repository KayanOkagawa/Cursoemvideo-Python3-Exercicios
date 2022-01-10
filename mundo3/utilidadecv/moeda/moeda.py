def aumentar(num, p, show=False):
    if show:
        return moeda(num + (num * (p/100)))
    else:
        return num + (num * (p/100))


def diminuir(num, p, show=False):
    if show:
        return moeda(num - (num * (p/100)))
    else:
        return num - (num * (p/100))


def dobro(num, show=False):
    if show:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, show=False):
    if show:
        return moeda(num / 2)
    else:
        return num / 2


def moeda(valor):
    return f'R${valor}'


def resumo(preco, pa, pd):
    print('-=' * 15)
    print('       RESUMO DO VALOR')
    print('-=' * 15)
    print(f"""Preço Analisado: {moeda(preco)}
Dobro do preço: {dobro(preco, True)}
Metade do preço: {metade(preco, True)}
{pa}% de aumento: {aumentar(preco, pa, True)}
{pd}% de redução: {diminuir(preco, pd, True)}""")
    print('-=' * 15)