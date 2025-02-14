#transforma apenas a primeira letra de uma string em maiuscula
nome = "gabriel"
print(nome.capitalize() ,"\n" )

#transforme todas as letras em minusculas
nome = "gabriel"
print(nome.casefold() ,"\n" )

#conta o numero de vezes que uma caractere especiifico aparece na string

nome = "gabrielbartholdy07@gmail.com"
print(nome.count("a") ,"\n" )

#retorne true ou false para um teste se a string termina com uma  string especifica

nome = "gabrielbartholdy07@gmail.com"
print(nome.endswith('gmail.com') ,"\n" )

#encontra a posição do termo procurado, lembre-se começa do zero

nome = "gabrielbartholdy07@gmail.com"
print(nome.find("@"),"\n" )

#verefiqye se o texto é todo feito com letras 

nome = 'gabriel'
print(nome.isalpha(),"\n")

#verefique se o texto é feito com num

nome="2432"
print(nome.isnumeric(),"\n")

#substitui um caractere escolhido por outro

nome = 'gabriel'
print(nome.replace('a','o'),"\n")

#separa o texto string baseado em algum caracter indicado

nome = 'gabriel @ ruan gostoso'
print(nome.split('@'),"\n")

#colocar todos as letras iniciais em maiscula

nome="gabriel de almeida bartholdy"
print(nome.title(),"\n")

#retira os caracter indesejados ,como por exemplo espaços que não agregram valor
nome = " gabriel de almeida BArthold"
print(nome.strip(),"\n")

#retorne true ou false para um teste de uma string se inicia com um texto especifico
nome="gabriel 2007"
print(nome.startswith("gab"),"\n")
print(nome.startswith("Gab"),"\n")