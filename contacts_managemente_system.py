# classe contactos com os campos nome, telefone e email
contact_list = []
details_option = None

class Contact:
    def __init__(self, nome, telemovel, email):
        self.name = nome
        self.mobile = telemovel
        self.email = email
        self.category = None

    def __str__(self) -> str:
        return self.name + " - " + str(self.mobile) + " | " + self.email

# lista de objetos do tipo contacto

def show_contacts():
    if len(contact_list) > 0:
        for contact in contact_list:
            print(contact.name, "\n")
        # print(f"{contact.name} - {contact.mobile} | {contact.email}")
    else:
        print("Lista de Contactos vazia.\n")

def see_contact(contact_id):
    print(contact_list[contact_id], "\n")
    
    details_option = int(input ("1 - Alterar contacto\n2 - Remover contacto.\n0 - Voltar\nO que deseja fazer? "))
    if details_option == 1:
        pass
    elif details_option == 2:
        print(contact_id)
        remove_contact(contact_id)
    elif details_option == 0:
        show_contacts()



def add_contact():
    print("----- ADICIONAR CONTACTO -----\n")
    nome = input("Nome : \n")
    telemovel = input("Telemóvel: \n")
    email = input("E-mail: \n")
    contact = Contact(nome, telemovel, email)
    contact_list.append(contact)
    print("Contacto adicionado com sucesso.")


def change_contact(contact_id):
    for contact[]


def remove_contact(contact_id):
    if contact_id < 0 and contact_id < len(contact_list):
        contact_list.pop(contact_id)
        print("Contacto eliminado com sucesso.")
    else:
        print("Contacto não encontrado. Nada foi removido.")
    

# menu - inserir e listar
menu_option = None

while True:
    print("----- LISTA DE CONTACTOS ------\n"
          "1 - Ver lista de contatos\n"
          "2 - Ver detalhes do contacto\n"
          "3 - Adicionar contacto\n"
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
    else:
        print(" A fechar aplicação...")
        quit()



# lista = [("nome: "), "tlm: ")]