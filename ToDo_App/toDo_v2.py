import sqlite3
connection = sqlite3.connect("ToDo_BD.db")

# Criar um cursor que indica a ligação en que estamos a trabalhar
cursor = connection.cursor()

# SQL não tem booleanos
cursor.execute('''
               create table if not exists tbl_tasks(
                id integer primary key AUTOINCREMENT,
                description varchar(150) not null,
                concluded integer not null default 0
               )
                ''')

def show_tasks():
    cursor.execute("Select * from tbl_tasks where concluded = 0")
    tasks = cursor.fetchall()
    if len(tasks) == 0:
        print("Não tem tarefas por fazer!")
    else:
        for task in tasks:
            print(task[0], " - ", task[1], "\n")

# + serve para concatenar o texto com a variável
def add_task():
    task = input("Insira a tarefa:\n")
    cursor.execute("Insert into tbl_tasks(description) values('"+task+"')")
    connection.commit()


def conclude_task():
    id_task = input("Indique a tarefa a concluir:\n")
    cursor.execute("Update tbl_tasks Set concluded = 1 where id = '"+id_task+"'")
    connection.commit()


def delete_task():
    id_task = input("Indique a tarefa a eliminar:\n")
    cursor.execute("Delete from tbl_tasks where id = '"+id_task+"'")
    connection.commit()


option = None
while option != "0":
    print(
        "-----------------------------------\n"
        "               MENU\n"
        "-----------------------------------\n"
        "1 - Listar tarefas\n"
        "2 - Adicionar tarefa\n"
        "3 - Alterar tarefa\n"
        "4 - Eliminar tarefa\n"
        "0 - Sair\n"
        )
    
    option = input("Escolha o que quer fazer: ")
    
    if option == "1":
        show_tasks()
    elif option == "2":
        add_task()
    elif option == "3":
        conclude_task()
    elif option == "4":
        delete_task()
    else:
        quit()
    