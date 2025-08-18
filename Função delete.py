l_nomes = []
def menu():
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - delete')
    print('[e] - exit')
def create():
        nome - input('Inserir - Nome:')
        l_nomes.append(nome)
def read():
    print("Valores da lista na horizontal")
    print(l_nomes)
def update ():
    indice = int(input("Atualizar - Qual posição (indice):"))
    novo_nome = input("Atualizar - Novo nome:")
    l_nomes [indice] = novo_nome
def delete():
    nome = input("Remover nome:")
    l_nome.remove(nome)
if __name__ == '__main__':
    while True:
        op = menu ()
        if op == 'c':
            create()
        elif op =='r':
            read()
        elif op == 'u':
            update()
        elif op =='d':
            delete()
        else:
            break