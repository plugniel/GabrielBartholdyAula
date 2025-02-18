
estoq = [100,50,330,34,24,42,54]
prod = ['coca','delvale','pepsi','licor','pepsi 0','agua','agua da serra']

nivel_minino = 50

for i,qtde in enumerate(estoq):
    if qtde < nivel_minino:
        print(prod[i],qtde)
