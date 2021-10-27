import csv
import os.path

list_agenda = []

def cadastrar():
    print("Cadastra Contato")
    contato = []
    contato.append(input("Nome:"))
    contato.append(input("Telefone:"))
    list_agenda.append(contato)
    print("Contato salvo com sucesso!")
    ordenar()
    input("Enter para sair")

def listar():
    for contato in list_agenda:
        print("Nome:",contato[0], " Telefone:",contato[1])
    input("Enter para sair")

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
            
def excluir():
    nome = input("Dgite o nome:")
    for i in range(len(list_agenda)):
        if nome == list_agenda[i][0]:
            del(list_agenda[i])
            print("Excluido com sucesso!")
            break
        
def ordenar():
    for i in range(len(list_agenda)):
        for j in range(len(list_agenda)):
            if list_agenda[i][0] < list_agenda[j][0]:
                aux = list_agenda[i]
                list_agenda[i] = list_agenda[j]
                list_agenda[j] = aux


def abrir_agenda():
    if os.path.isfile("agenda.txt"):
        with open("agenda.txt", 'r') as arquivo:
            contatos = csv.reader(arquivo,delimiter=",")
            for linha in contatos:
                list_agenda.append(linha)

def salvar_arq():
    with open("agenda.txt", 'w') as arquivo:
        contatos = csv.writer(arquivo,delimiter=",")
        contatos.writerows(list_agenda)
        
            
def clear(linhas):
    print("\n"*linhas)

def funcao_menu(op):
    if op == 1:
        cadastrar()
    elif op == 2:
        listar()
    elif op == 3:
        buscar()
    elif op == 4:
        alterar()
    elif op == 5:
        excluir()
    elif op == 6:
        ordenar()
    
def menu():
    op = 1
    abrir_agenda() 
    while op != 0:
        clear(100)
        print("1-cadastrar")
        print("2-listar")
        print("3-buscar por nome")
        print("4-Alterar")
        print("5-excluir")
        print("6-Ordenar")
        print("0-sair")
        op = int(input("Digite:"))
        clear(100)
        funcao_menu(op)
    salvar_arq()  

   
menu()



