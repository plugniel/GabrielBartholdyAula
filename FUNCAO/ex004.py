def get_nome():
    nome_usu = input('Entre com o seu nome: ')
    return nome_usu

def print_mensagem(nome_usu):
    print('Ola jovem padawan',nome_usu)

def main():
    nome_usu = get_nome()
    print_mensagem(nome_usu)

main()