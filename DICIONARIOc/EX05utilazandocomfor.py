mais_v = {'tech':'iphone','refri':"consul 1200",'livros':'o alquimista','eletrodom':'geladeira'}

for chave in mais_v:
    print('A categoria {} temos o produto {}'.format(chave,mais_v[chave]))

#for ite in mais_v.items():
    #print(ite)


for ite,oq in mais_v.items():
    print('{}:{}'.format(ite,oq))
