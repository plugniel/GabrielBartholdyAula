#faça um progrma que o usuario digite um numero e diga se o numero é superior a 20,inferior a 10 ou se esta entre 10 e 20
number = int(input("Qual o seu numero?"))

if number > 20:
    print("seu numero é superior a 20")
elif number <10:
    print("seu numero é menor de 10")
else:
    print("Esta entre 10 e 20")