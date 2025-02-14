#faça um programa que receba uma nota do aluno e se for superior ou igual a 7 apareça mensagen de aprovado , se for inferior a 5 "não aprovado\reprovad direto"e se estiver entre 5 e 7 fale "não aprovado\recuperação"

nota = int(input("Qual sua nota?"))

if nota >= 7:
    print("Aprovado")
else:
    if nota < 5 :
        print("Reprovado direto")
    else:
        print("recuperação")   