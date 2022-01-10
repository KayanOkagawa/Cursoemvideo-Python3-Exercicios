from utilidadecv.moeda import moeda

preco = float(input('Digite o Valor: R$'))
print(f'A Metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O Dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'O Aumento de 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13))}')
