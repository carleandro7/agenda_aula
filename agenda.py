list_agenda = []

def cadastrar():
    nome = input("Nome:")
    telefone = input("Telefone:")
    contato = []
    contato.append(nome)
    contato.append(telefone)
    list_agenda.append(contato)
    print("Contato salvo com sucesso!")


def listar():
    for contato in list_agenda:
        print("Nome:",contato[0], " Telefone:",contato[1])

def buscar():
    nome = input("Digite o nome de busca:")
    for contato in list_agenda:
        if nome == contato[0]:
            print("Telefone:",contato[1])

def alterar():
    nome = input("Digite o nome de busca:")
    for contato in list_agenda:
        if nome == contato[0]:
            contato[0] = input("Novo nome:")
            contato[1] = input("Novo telefone:")

def menu():
    op = 1
    while op != 0:
        print("1-cadastrar")
        print("2-listar")
        print("3-buscar por nome")
        print("4-Alterar")
        print("0-sair")
        op = int(input("Digite:"))
        if op == 1:
            cadastrar()
        elif op == 2:
            listar()
        elif op == 3:
            buscar()
        elif op == 4:
            alterar()

    
menu()


