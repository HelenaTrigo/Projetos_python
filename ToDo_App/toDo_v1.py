import sqlite3
connection = sqlite3.connect("ToDo_DB.db")

print("Lista de Tarefas - v1")

tasks_list = []
option = None


def show_list():
    counter = 0

    print("POR FAZER")
    print(len(tasks_list), " tarefa(s) por fazer")
    for task in tasks_list:
        if tasks_list:
            counter += 1
            print(counter, "- ", task)


def create_task():
    new_task = input("Digite a nova tarefa a adicionar:\n")
    tasks_list.append(new_task)


def change_task():
    selected_task = int(input("Indique o número da tarefa que quer eliminar: "))
    tasks_list[selected_task - 1] = input("Digite a tarefa com alteração:\n")


def delete_task():
    deleted_task = int(input("Indique número da tarefa que quer eliminar: "))
    tasks_list.pop(deleted_task - 1)


while option != 0:
    print(
        " --------------------------\n"
        "           MENU\n",
        "--------------------------\n"
        "1 - Listar tarefas\n"
        "2 - Inserir tarefa\n"
        "3 - Alterar tarefa\n"
        "4 - Eliminar tarefa\n"
        "0 - Sair\n"
        "--------------------------"
    )

    option = input("Escolha uma opção: ")

    if option == "1":
        show_list()
    elif option == "2":
        create_task()
    elif option == "3":
        change_task()
    elif option == "4":
        delete_task()
    else:
        quit()


