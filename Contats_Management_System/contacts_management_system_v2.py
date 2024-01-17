# ligação à base de dados
import sqlite3
connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()

# Definição das funções
def show_contacts():
    print("------ LISTA DE CONTACTOS ------")
    cursor.execute("Select id, name from Contacts order bu name")
    contacts_list = cursor.fetchall()
    if len(contacts_list) <= 0:
        print("Lista de contactos vazia.)")
    else:
        print(f"Número de contactos: {len(contacts_list)}\n")
        for contact in contacts_list:
            print(f"{contact[0]} - {contact[1]}")


def see_contact(contact_id):
    cursor.execute("select * from Contacts where id = '{contact_id}'")
    contact_detais = cursor.fetchone()
    print(f"{contact_detais[1]} - {contact_detais[2]} | {contact_detais[4]}\N
          {contact_detais[3]}"
            )
    details_option = int(input ("1 - Alterar contacto\n2 - Remover contacto.\n3 - Adicionar o contacto a uma categoria.\n0 - Voltar\nO que deseja fazer? "))
    if details_option == 1:
        # change_contact(contact_id)
        pass
    elif details_option == 2:
        print(contact_id)
        remove_contact(contact_id)
    elif details_option == 3:
        # add_to_category(contact_id)
        pass
    elif details_option == 0:
        show_contacts()

def add_contact():
    print("----- ADICIONAR CONTACTO -----\n")
    nome = input("Nome : \n").capitalize()
    telemovel = input("Telemóvel: \n")
    email = input("E-mail: \n")
    cursor.execute("Insert into Contacts(name, mobile, email) values('{nome}', '{telemovel}', '{email}')")
    connection.commit()
    print("Contacto adicionado com sucesso.\n")

def change_contact(id_contact):
    print("------ EDITAR CONTACTO ------")
    change_name = input("Alterar nome? [S/N]").upper() == "S"
    if change_name:
        new_name = input("Nome: ").capitalize()
        if new_name != "":
            cursor.execute("update Contacts set name = '{new_name}' where id = '{contact_id}'")
            print("\nNome atualizado com sucesso.\n")
    else:
        print("\nNome não foi alterado.\n")
    
    change_number = input("Alterar número de telemóvel? [S/N]").upper() == "S"
    if change_number:
        change_option = int(input("1 - Editar o número atual.\n2 - Adicionar um número alternativo. \n"))
        if change_option == 1:
            edited_mobile = input("telemóvel: ")
            cursor.execute("update Contacts set mobile = '{edited_mobile}' where id = '{contact_id}'")
            print("\nTelemóvel atualizado com sucesso.\n")
        elif change_option == 2:
            other_mobile = input("Telemóvel alternativo: ")
            cursor.execute("update Contacts set other_mobile = '{other_mobile}' where id = '{contact_id}'")
            print("\nTelemóvel alternativo adicionado com sucesso.\n")
        else:
            print("Telemóvel não foi atualizado.\n")
    
    change_email = input("Alterar e-mail? [S/N]").upper() == "S"
    if change_email:
        new_email = input("E-mail: ")
        cursor.execute("update Contacts set email = '{new_email}' where id = '{contact_id}'")
        print("\nE-mail atualizado com sucesso\n")
    else:
        print("E-mail não foi atualizado.\n")
    
    cursor.commit()
    print("Contacto atualizado com sucesso.")

def remove_contact(contact_id):
    cursor.execute("delete Contacts where id = '{contact_id}")
    connection.commit()
    print("Contacto removido com sucesso.")


def add_to_category(id_contact):
    cursor.execute("Select * from Categories")
    categories_list = cursor.fetchall()
    for category in categories_list:
        print(f"{categories_list[0] + 1} - {categories_list[1]}")
    category_id = int(input("Indique a que categoria quer adicionar o contacto: ")) - 1
    cursor.execute("update Contacts set category = categories_list[{category_id}]")
    connection.commit()
    print("Foi associado uma categoria ao seu contacto.")




# criação das tabelas
cursor.execute("""create table if not exists 'Contacts'(
                id integer primary key,
                name text not null,
                mobile text not null,
                other_mobile text null,
                email text null
                category integer null foreign key references Categorias(id)
                )
               """)

cursor.execute("""create table if not exists 'Categories'(
                   id integer primary key,
                   category text not null
                )
               """)

# criar relação entre as tabelas
'''cursor.execute("ALTER TABLE Contactos
                ADD CONSTRAINT FK_Category
                FOREIGN KEY (category) REFERENCES Categorias(id)")
conneciton.commit()
'''

# menu App
menu_option = None

while True:
    print("----- LISTA DE CONTACTOS ------\n"
          "1 - Ver lista de contatos\n"
          "2 - Ver detalhes do contacto\n"
          "3 - Adicionar contacto\n"
          "4 - Criar nova categoria\n"
          "0 - Sair\n"
          )
    
    menu_option = input("Escolha o que pretende fazer: ")
    print("")

    if menu_option == "1":
        show_contacts()
    elif menu_option == "2":
        contact_id = int(input("Indique o Id do contacto que quer ver os detalhes: ")) - 1
        see_contact(contact_id)
    elif menu_option == "3":
        add_contact()
    elif menu_option == "4":
        new_category = input("Digite a categoria a criar: ")
        cursor.execute("insert into Categorias(name) values('{new_category}')")
        connection.commit()
        print("\n Categoria adicionada com sucesso.\n")
    else:
        print(" A fechar aplicação...")
        # termina ligação à BD
        connection.close()
        quit()