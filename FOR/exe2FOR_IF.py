vendas = [100,50,30,34,24,42,54,34,23,65,32,23,12,54,67,32,12,53,655]
meta = 100
qtdmeta= 0
for venda in vendas:
    if venda >= meta:
        qtdmeta += 1
qtdfun = len(vendas)
print('O percentual foi de {:.1%}'.format(qtdmeta/qtdfun))