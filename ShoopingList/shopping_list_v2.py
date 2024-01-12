import sqlite3

connection = sqlite3.connect("shooping_list_DB.db")
cursor = connection.cursor()


def view_list():
    print("----- Lista de Compras -----")
    cursor.execute("select count(*) from shopping")
    tt_itens = cursor.fetchone()
    if tt_itens[0] == 0:
        print("A sua lista de compras está vazia!")
    else:
        print (f"Total de itens a comprar: {tt_itens[0]}")
        for row in cursor.execute("select rowid, * from shopping"):
            print(row[0], " - ", row[1], ":", row[2])

def add_item():
    item = input("Introduza o item a comprar: \n")
    qty = input("Introduza a quantidade a comprar: ")
    if qty == "":
        qty = 1
    cursor.execute("Insert into shopping(item, quantity) values('"+item+"','"+qty+"')")
    connection.commit()
    print("Item adicionado com sucesso.")


def change_item():
    item_id = input("Indique o item a alterar:\n")
    cursor.execute("select rowid from shopping")
    #itens_id_list = cursor.fetchall()
    #print(itens_id_list)
    #if x == item_id:
    cursor.execute("select item from shopping where rowid = '"+item_id+"'")
    item = cursor.fetchone()
    print(f"A alterar o item {item}...")
    qty = input("Introduza a nova quantidade a alterar: ")
    cursor.execute("Update shopping set quantity = '"+qty+"' where rowid = '"+item_id+"'")
    connection.commit()
    print("Item alterado com sucesso.")
    #else:
        #print("O item não existe na sua lista de compras.")


def delete_item():
    item = input("Indique o item a eliminar: ")
    cursor.execute("delete from shopping where rowid = '"+item+"'")
    connection.commit()
    print("Item apagado com sucesso.")

def delete_list():
    confirmation = input("Depois de apagar a lista a acção será IRREVERSÌVEL!. Deseja continuar? [S/N] ").upper()
    if confirmation == "S":
        cursor.execute("Delete from shopping")
        connection.commit()
        print("Lista eliminada com suceso!")
    else:
        print("Cancelado! A sua lista não foi eliminada, boas compras!")

# criar tabela, com rowid automatico
cursor.execute("""
               create table if not exists shopping(
                item text not null,
                quantity integer not null default 1
               )
               """)

while True:
    print("---------- APP DE COMPRAS -----------")
    print("""
         ------------ MENU -----------
          1 - Mostrar lista 
          2 - Inserir item 
          3 - Alterar item
          4 - Apagar item
          5 - Apagar lista
          0 - Sair \n
          """)
    
    option = None
    
    option = int(input("Escolha a sua opção: "))

    if option == 1:
        view_list()
    elif option == 2:
        add_item()
    elif option == 3:
        change_item()
    elif option == 4:
        delete_item()
        view_list()
    elif option == 5:
        delete_list()
    else:
        quit()