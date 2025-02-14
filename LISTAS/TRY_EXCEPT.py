produtos = ['tv','celular','mouse','teclado','geladeira','forno']
item = input('Qual item deseja remover?')

try:
    produtos.remove(item)
    print(produtos)
except:
    print("o produto {} não existe".format(item))