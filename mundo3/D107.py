from utilidadecv.moeda import moeda

print('MODULARIZAÇÃO')
print('-=' * 30)
preco = float(input('\nDigite o Valor: R$'))
print(f'A Metade de {preco} é {moeda.metade(preco)}')
print(f'O Dobro de {preco} é {moeda.dobro(preco)}')
print(f'O Aumento de 10%, temos {moeda.aumentar(500, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(500, 13)}')
