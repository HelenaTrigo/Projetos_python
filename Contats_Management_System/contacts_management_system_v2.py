# ligação à base de dados
import sqlite3
connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()

# Definição das funções
def show_contacts():
    all_categories_list = []
    tt_contacts = 0
    print("------ LISTA DE CONTACTOS ------")
    cursor.execute("select count(id) from Categories")
    max_range = cursor.fetchone()
   
    for _ in range(1, max_range[0] + 1):
        cursor.execute(f'''
                        SELECT id, name FROM Contacts 
                            where id_category = {_}
                            order by name''')
        category_list = cursor.fetchall()
        tt_contacts  += len(category_list)
        all_categories_list.append(category_list)
    
    print(f"Número de contactos: {tt_contacts}\n")
    if  tt_contacts <= 0:
        print("Lista de contactos vazia.\n")
    else:
        cursor.execute("select count(id) from Categories")
        max_range = cursor.fetchone()
        
        for _ in range(1, max_range[0] + 1):
            cursor.execute(f"select category from Categories where id = {_}")
            category_name = cursor.fetchone()
            print(f"----- CONTACTOS EM {category_name[0].upper()} -----")
            if len(all_categories_list[_ - 1]) <= 0:
                    print(f"Sem contactos na categoria {category_name[0].capitalize()}.")
            else:
                for contact in all_categories_list[_ - 1]:
                    print(f"{contact[0]} - {contact[1]}")
            print("")


def see_contact(contact_id):
    cursor.execute(f"select Contacts.id, name, mobile, ifnull(email, 'sem email'), ifnull(other_mobile, 'sem contacto'), category from Contacts left join Categories on id_category = Categories.id where Contacts.id = '{contact_id}'")
    contact_detais = cursor.fetchone()
    print(f"{contact_detais[5]}\n{contact_detais[1]} - {contact_detais[2]} | {contact_detais[3]}\nTelemóvel alternativo: {contact_detais[4]}")
   
    details_option = int(input ("1 - Alterar contacto\n2 - Remover contacto.\n3 - Adicionar o contacto a uma categoria.\n0 - Voltar\nO que deseja fazer? "))
    if details_option == 1:
        change_contact(contact_id)
    elif details_option == 2:
        print(contact_id)
        remove_contact(contact_id)
    elif details_option == 3:
        add_to_category(contact_id)
        pass
    elif details_option == 0:
        show_contacts()

def add_contact():
    print("----- ADICIONAR CONTACTO -----\n")
    nome = input("Nome : \n").capitalize()
    telemovel = input("Telemóvel: \n")
    email = input("E-mail: \n")
    if email == '':
        email = None
        cursor.execute("Insert into Contacts(name, mobile) values('"+nome+"', '"+telemovel+"')")
    else:
          cursor.execute("Insert into Contacts(name, mobile, email) values('"+nome+"', '"+telemovel+"', '"+email+"')")
    connection.commit()
    print("Contacto adicionado com sucesso.\n")

def change_contact(id_contact):
    print("------ EDITAR CONTACTO ------")
    change_name = input("Alterar nome? [S/N]").upper() == "S"
    if change_name:
        new_name = input("Nome: ").capitalize()
        if new_name != "":
            cursor.execute(f"update Contacts set name = '{new_name}' where id = {contact_id}")
            print("\nNome atualizado com sucesso.\n")
    else:
        print("\nNome não foi alterado.\n")
    
    change_number = input("Alterar número de telemóvel? [S/N]").upper() == "S"
    if change_number:
        change_option = int(input("1 - Editar o número atual.\n2 - Adicionar um número alternativo. \n"))
        if change_option == 1:
            edited_mobile = input("telemóvel: ")
            cursor.execute(f"update Contacts set mobile = '{edited_mobile}' where id = '{contact_id}'")
            print("\nTelemóvel atualizado com sucesso.\n")
        elif change_option == 2:
            other_mobile = input("Telemóvel alternativo: ")
            cursor.execute(f"update Contacts set other_mobile = '{other_mobile}' where id = '{contact_id}'")
            print("\nTelemóvel alternativo adicionado com sucesso.\n")
        else:
            print("Telemóvel não foi atualizado.\n")
    
    change_email = input("Alterar e-mail? [S/N]").upper() == "S"
    if change_email:
        new_email = input("E-mail: ")
        cursor.execute(f"update Contacts set email = '{new_email}' where id = '{contact_id}'")
        print("\nE-mail atualizado com sucesso\n")
    else:
        print("E-mail não foi atualizado.\n")
    
    connection.commit()
    print("Contacto atualizado com sucesso.")

def remove_contact(contact_id):
    cursor.execute(f"delete from Contacts where id = {contact_id}")
    connection.commit()
    print("Contacto removido com sucesso.")


def add_to_category(contact_id):
    cursor.execute("Select * from Categories")
    categories_list = cursor.fetchall()
    for category in categories_list:
        print(f"{category[0]} - {category[1]}")
    category_id = int(input("Indique a que categoria quer adicionar o contacto: "))
    while category_id > len(categories_list):
        print("Erro!! A categoria selecionada não existe!")
        category_id = int(input("Indique a que categoria quer adicionar o contacto: "))
    cursor.execute(f"update Contacts set id_category = {category_id} where Contacts.id = {contact_id}")
    connection.commit()
    print("Foi associado uma categoria ao seu contacto.")




# criação das tabelas
cursor.execute("""create table if not exists 'Contacts'(
                    id integer primary key,
                    name text not null,
                    mobile text not null,
                    other_mobile text null,
                    email text null,
                    id_category integer not null default 1, foreign key (id_category)
                        references Categories(id)
                            on delete set null
                            on update cascade
                    )
               """)

cursor.execute("""create table if not exists 'Categories'(
                   id integer primary key,
                   category text not null
                )
               """)

cursor.execute("select * from Categories")
categories_list = cursor.fetchall()
if len(categories_list) <= 0:
    cursor.execute("insert into Categories(category) values('Geral'), ('Família'), ('Trabalho'), ('Amigos')")   
connection.commit()

# criar relação entre as tabelas se ainda não existir
'''cursor.execute("ALTER TABLE Contacts
                ADD CONSTRAINT FK_Category
                FOREIGN KEY (category) REFERENCES Categories(id)")
conneciton.commit()
'''

# menu App
menu_option = None

while True:
    print("----- MENU DE CONTACTOS ------\n"
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
        contact_id = int(input("Indique o id do contacto que quer ver os detalhes: "))
        see_contact(contact_id)
    elif menu_option == "3":
        add_contact()
    elif menu_option == "4":
        new_category = input("Digite a categoria a criar: ")
        cursor.execute("insert into Categories(category) values('"+new_category+"')")
        connection.commit()
        print("\n Categoria adicionada com sucesso.\n")
    else:
        print(" A fechar aplicação...")
        # termina ligação à BD
        connection.close()
        quit()