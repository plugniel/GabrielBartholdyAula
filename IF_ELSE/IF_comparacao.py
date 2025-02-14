fatu = int(input("Qual foi o faturamento da loja esse mes?"))
custo = int(input("Qual foi o custo loja nesse mes?"))
lucro = fatu - custo
if custo and fatu :
    lucro = fatu - custo
    print("o lucro foi de {}".format(lucro))    
else:
    print("Campos invalidos")

