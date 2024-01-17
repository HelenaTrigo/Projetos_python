# definição de listas e variáveis
contacts_list = []
categories_list = ["trabalho", "família", "favoritos", "IEFP"]
details_option = None


# criação da classe e seus métodos
class Contact:
    def __init__(self, nome, telemovel, email):
        self.name = nome
        self.mobile = telemovel
        self.other_mobile = None
        self.email = email
        self.category = None

    # usada quando tento imprimir a lista de objetos
    def __str__(self) -> str:
        if not self.category and not self.other_mobile:
            return self.name + " - " + str(self.mobile) + " | " + self.email
        if self.category and self.other_mobile:
            return self.category +"\n" + self.name + " - " + str(self.mobile) + " | " + self.email + "\nTelemóvel aternativo: " + str(self.other_mobile)
        if self.category or self.other_mobile:
            if self.category:
                return self.category +"\n" + self.name + " - " + str(self.mobile) + " | " + self.email
            elif self.other_mobile:
                return self.name + " - " + str(self.mobile) + " | " + self.email + "\nTelemóvel aternativo: " + str(self.other_mobile)
    
    
    # usada quando tento ordenar ascendente a lista
    def __lt__(self, other):
        return self.name < other.name


def show_contacts():
    if len(contacts_list) > 0:
        contacts_list.sort()
        for contact in contacts_list:
            print(f"{contacts_list.index(contact) + 1} - {contact.name}")
        # print(f"{contact.name} - {contact.mobile} | {contact.email}")
    else:
        print("Lista de Contactos vazia.\n")


def see_contact(contact_id):
    print("------ DETALHES DO CONTACTO ------")
    print(contacts_list[contact_id], "\n")
    
    details_option = int(input ("1 - Alterar contacto\n2 - Remover contacto.\n3 - Adicionar o contacto a uma categoria.\n0 - Voltar\nO que deseja fazer? "))
    if details_option == 1:
        change_contact(contact_id)
    elif details_option == 2:
        print(contact_id)
        remove_contact(contact_id)
    elif details_option == 3:
        add_to_category(contact_id)
    elif details_option == 0:
        show_contacts()


def add_contact():
    print("----- ADICIONAR CONTACTO -----\n")
    nome = input("Nome : \n").capitalize()
    telemovel = input("Telemóvel: \n")
    email = input("E-mail: \n")
    contact = Contact(nome, telemovel, email)
    contacts_list.append(contact)
    print("Contacto adicionado com sucesso.\n")


def change_contact(contact_id):
    print("------ EDITAR CONTACTO ------")
    change_name = input("Alterar nome? [S/N]").upper() == "S"
    if change_name:
        new_name = input("Nome: ")
        if new_name != "":
            contacts_list[contact_id].name = new_name
            print("\nNome atualizado com sucesso.\n")
    else:
        print("\nNome não foi alterado.\n")
    
    change_number = input("Alterar número de telemóvel? [S/N]").upper() == "S"
    if change_number:
        change_option = int(input("1 - Editar o número atual.\n2 - Adicionar um número alternativo. \n"))
        if change_option == 1:
            edited_mobile = input("telemóvel: ")
            contacts_list[contact_id].mobile = edited_mobile
            print("\nTelemóvel atualizado com sucesso.\n")
        elif change_option == 2:
            other_mobile = input("Telemóvel alternativo: ")
            contacts_list[contact_id].other_mobile = other_mobile
            print("\nTelemóvel alternativo adicionado com sucesso.\n")
        else:
            print("Telemóvel não foi atualizado.\n")
    
    change_email = input("Alterar e-mail? [S/N]").upper() == "S"
    if change_email:
        new_email = input("E-mail: ")
        contacts_list[contact_id].email = new_email
        print("\nE-mail atualizado com sucesso\n")
    else:
        print("E-mail não foi atualizado.\n")
    

def remove_contact(contact_id):
    print("------- REMOVER CONTACTO -------")
    if contact_id > 0 and contact_id < len(contacts_list):
        contacts_list.pop(contact_id)
        print("Contacto eliminado com sucesso.\n")
    else:
        print("Contacto não encontrado. Nada foi removido.\n")


def add_to_category(contact_id):
    for category in categories_list:
        print(f"{categories_list.index(category) + 1} - {category}")
    category_id = int(input("Indique a que categoria quer adicionar o contacto: "))
    contacts_list[contact_id].category = categories_list[category_id]

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
        categories_list.append(new_category)
        print("\n Categoria adicionada com sucesso.\n")
    else:
        print(" A fechar aplicação...")
        quit()

