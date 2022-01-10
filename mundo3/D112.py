from utilidadecv.dados import dados
from utilidadecv.moeda import moeda

p = dados.leia_dinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)
