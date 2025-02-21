produtos = ['tv','celular','mouse','teclado','tablet']
vendas = [1000 , 1500 , 350 , 270 , 900]
print("as vendas de {} foram de {}".format(produtos[2],format(vendas[2])))

produtos = ['tv','celular','mouse','teclado','tablet']
i = produtos.index("mouse")

print('o valor de i é '+str(i))
print('o produto da posição i é '+str(produtos[i]))


produtos = ['tv','celular','mouse','teclado','geladeira','forno']
estoque = [1000 , 1500 , 350 , 270 , 900,80]
produto = input('insira o nome do produto em letra minuscula: ')
if  produto in produtos:
    
    produtos.index(produto)
    qtde = estoque[i]
    print('temos {} unidades de {} no estoque'.format(qtde,produto))
else:
    print("produto não cadastrado")