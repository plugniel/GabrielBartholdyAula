venda = input('Registre um produto.para cancelar o registre de um novo produto,basta apertar nd (enter)')
vendas = []

while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto.para cancelar o registre de um novo produto,basta apertar nd (enter)')
print('Registro finalizado, as vendas foram: {}'.format(vendas))