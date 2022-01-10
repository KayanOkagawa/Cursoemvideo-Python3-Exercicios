from utilidadecv.moeda import moeda

preco = float(input('Digite o Preço: '))
print(f'A Metade de {moeda.metade(preco, show=True)}')
print(f'O Dobro de {moeda.dobro(preco, show=True)}')
print(f'O Aumento de 10%, temos {moeda.aumentar(preco, 10, show=True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, show=True)}')
